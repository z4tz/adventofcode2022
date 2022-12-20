import os
from inputreader import aocinput


def surface_area(data: list[str]) -> int:
    cubes = {}
    for line in data:
        cube = tuple(int(part) for part in line.strip().split(','))
        cubes[cube] = 6
        for neighbor in [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]:
            if (tempcube := tuple(a + b for a, b in zip(cube, neighbor))) in cubes:
                cubes[cube] -= 1
                cubes[tempcube] -= 1
    return sum(cubes.values())


def main(day):
    data = aocinput(day)

    result = surface_area(data)
    print(result)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
