import os
from inputreader import aocinput

neighbors = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]


def surface_area(data: list[str]) -> tuple[int, int]:
    cubes = {}
    extreme_values = None
    for line in data:
        cube = tuple(int(part) for part in line.strip().split(','))
        if extreme_values:
            for value, minmax in zip(cube, extreme_values):
                if value < minmax[0]:
                    minmax[0] = value
                elif value > minmax[1]:
                    minmax[1] = value
        else:
            extreme_values = ([cube[0], cube[0]], [cube[1], cube[1]], [cube[2], cube[2]])  # start values

        cubes[cube] = 6
        for neighbor in neighbors:
            if (tempcube := tuple(a + b for a, b in zip(cube, neighbor))) in cubes:
                cubes[cube] -= 1
                cubes[tempcube] -= 1

    # part 2, for each cube outside, check if neighbor is lava
    visited = set()
    to_visit = {(extreme_values[0][0] - 1, extreme_values[1][0] - 1, extreme_values[2][0] - 1)}
    surface_count = 0
    while to_visit:
        current = to_visit.pop()
        visited.add(current)
        for neighbor in neighbors:
            tempcube = tuple(a + b for a, b in zip(current, neighbor))
            if all([extreme_values[i][0] - 1 <= coord <= extreme_values[i][1] + 1 for i, coord in
                    enumerate(tempcube)]) and tempcube not in visited:

                if tempcube in cubes:
                    surface_count += 1
                else:
                    to_visit.add(tempcube)

    return sum(cubes.values()), surface_count


def main(day):
    data = aocinput(day)
    result = surface_area(data)
    print(result)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
