import os
from inputreader import aocinput
from typing import List, Tuple, Set
import numpy as np


def get_neighbors(p: [int, int], shape: np.shape) -> List[tuple[int, int]]:
    valid_neighbors = []
    for x, y in [(p[0] - 1, p[1]), (p[0] + 1, p[1]), (p[0], p[1] - 1), (p[0], p[1] + 1)]:
        if 0 <= x < shape[0] and 0 <= y < shape[1]:
            valid_neighbors.append((x, y))
    return valid_neighbors


def get_shortest(heights: np.ndarray, start: Tuple[int, int], end: Set[tuple], condition: callable) -> int:
    steps = 0
    visited = {start}
    to_visit = {start}
    while True:
        steps += 1
        to_visit_next = set()
        for current in to_visit:
            visited.add(current)
            for neighbor in get_neighbors(current, heights.shape):
                if condition(heights[neighbor], heights[current]) and neighbor not in visited:
                    if neighbor in end:
                        return steps
                    to_visit_next.add(neighbor)
        to_visit = to_visit_next


def shortest_path(data: List[str]) -> Tuple[int, int]:
    heights = np.array(np.array([[ord(char) for char in line.strip()] for line in data]))
    start = tuple(zip(*np.nonzero(heights == ord('S'))))[0]
    end = tuple(zip(*np.nonzero(heights == ord('E'))))[0]
    heights[start] = ord('a')
    heights[end] = ord('z')

    steps = get_shortest(heights, start, {end}, lambda x, y: x - y <= 1)

    # part 2
    # start from end and find one of the lowest positions
    lowest_positions = set(zip(*np.nonzero(heights == ord('a'))))
    steps2 = get_shortest(heights, end, lowest_positions, lambda x, y: y - x <= 1)

    return steps, steps2


def main(day):
    data = aocinput(day)
    result = shortest_path(data)
    print(result)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
