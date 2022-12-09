import os
from inputreader import aocinput
from typing import List

directions = {'R': 1, 'L': -1, 'U': 1j, 'D': -1j}


def movement(front: complex, back: complex) -> complex:
    if abs(diff := front - back) >= 2:
        real = diff.real and diff.real / abs(diff.real)  # avoid divide by zero issue
        imag = diff.imag and diff.imag / abs(diff.imag)
        return back + complex(real, imag)
    return back


def tail_visits(data: List[str], rope_length) -> int:
    rope = [0+0j] * rope_length
    visited = set()
    for line in data:
        direction, steps = line.strip().split()
        for i in range(int(steps)):
            rope[0] += directions[direction]
            for rope_part in range(1, len(rope)):
                rope[rope_part] = movement(rope[rope_part - 1], rope[rope_part])
            visited.add(rope[-1])
    return len(visited)


def main(day):
    data = aocinput(day)
    result = tail_visits(data, 2)
    result2 = tail_visits(data, 10)
    print(result, result2)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
