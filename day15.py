import os
from inputreader import aocinput
import re
from itertools import combinations, pairwise, chain


def beacons(data: list[str], inspection_row, max_limit) -> tuple[int, int]:
    regex = re.compile(r"^Sensor at x=(-?\d*), y=(-?\d*): closest beacon is at x=(-?\d*), y=(-?\d*)$")
    intervals = []
    sensors = []
    for line in data:
        values = [int(value) for value in regex.match(line).groups()]
        distance = abs(values[0] - values[2]) + abs(values[1] - values[3])
        sensors.append((values[0], values[1], distance + 1))  # +1
        if abs(values[1] - inspection_row) <= distance:
            x_width = (distance - abs(values[1] - inspection_row))
            intervals.append([values[0] - x_width, values[0] + x_width])

    intervals.sort()
    # Join intervals together
    joined_intervals = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] > joined_intervals[-1][1]:
            joined_intervals.append(interval)
        else:
            for joined_interval in joined_intervals:
                if interval[0] <= joined_interval[1]:
                    joined_interval[1] = max([joined_interval[1], interval[1]])
    intersections = set()
    for sensor1, sensor2 in list(combinations(sensors, 2)):
        intersections.update(find_intersections(sensor1, sensor2))

    valid = None
    for intersection in intersections:
        if not any([invalid_beacon(sensor, intersection, max_limit) for sensor in sensors]):
            valid = intersection
    return sum([interval[1] - interval[0] for interval in joined_intervals]), valid[0] * max_limit + valid[1]


def invalid_beacon(sensor, point, maxlim) -> bool:
    if point[0] < 0 or point[0] > maxlim or point[1] < 0 or point[1] > maxlim:
        return True
    return abs(sensor[0] - point[0]) + abs(sensor[1] - point[1]) <= sensor[2]-1


def get_corners(x0: int, y0: int, distance: int) -> tuple[int, int]:
    for x, y in [[distance, 0], [0, distance], [-distance, 0], [0, -distance]]:
        yield x0 + x, y0 + y


def findIntersection(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, x4: int, y4: int) -> tuple[float, float]:
    try:
        px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / (
                (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
        py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / (
                (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    except ZeroDivisionError:
        print('zerodivsion')
        return None
    return px, py


def valid_intersection(sensor, point) -> bool:
    return abs(sensor[0] - point[0]) + abs(sensor[1] - point[1]) <= sensor[2]


def find_intersections(sensor1: tuple[int, int, int], sensor2: tuple[int, int, int]) -> list:
    if abs(sensor1[0] - sensor2[0]) + abs(sensor1[1] - sensor2[1]) > sensor1[2] + sensor2[2]:  # no intersections
        return []

    corners1 = list(get_corners(*sensor1))
    corners1.append(corners1[0])  # add first corner again to get last line
    lines1 = list(pairwise(corners1))

    corners2 = list(get_corners(*sensor2))
    corners2.append(corners2[0])  # add first corner again to get last line
    lines2 = list(pairwise(corners2))

    line_combinations = []
    for i in range(4):
        line_combinations.append([lines1[i], lines2[(i + 1) % 4]])
        line_combinations.append([lines1[i], lines2[(i + 3) % 4]])

    intersections = []
    for line1, line2 in line_combinations:
        result = findIntersection(*chain(*line1, *line2))
        if result and valid_intersection(sensor1, result) and valid_intersection(sensor2, result):
            intersections.append(result)

    return intersections


def main(day):
    data = aocinput(day)
    result = beacons(data, 2000000, 4000000)
    print(result)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
