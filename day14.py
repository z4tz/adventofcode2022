import os
from inputreader import aocinput


def overflow(data: list[str]) -> tuple[int, int]:
    rock_coordinates = set()
    for line in data:
        coordinates = []
        for parts in line.strip().split('->'):
            x, y = parts.split(',')
            coordinates.append([int(x), int(y)])
        for i in range(len(coordinates)-1):
            if coordinates[i][0] == coordinates[i+1][0]:
                x = coordinates[i][0]
                y_start, y_end = sorted([coordinates[i][1], coordinates[i+1][1]])
                for y in range(y_start, y_end+1):
                    rock_coordinates.add(complex(x,y))
            else:
                y = coordinates[i][1]
                x_start, x_end = sorted([coordinates[i][0], coordinates[i + 1][0]])
                for x in range(x_start, x_end+1):
                    rock_coordinates.add(complex(x, y))
    abyss_start = int(max(rock_coordinates, key=lambda coord: coord.imag).imag)  # highest value is "lowest"
    rock_coordinates2 = rock_coordinates.copy()

    sandcount = 0
    landed = True
    while landed:
        landed = drop_sand(abyss_start, rock_coordinates)
        sandcount += 1

    # add floor to part 2
    y = abyss_start + 2
    for x in range(500 - (y + 1), 500 + (y + 1) + 1):
        rock_coordinates2.add(complex(x, y))

    sandcount2 = 0
    while 500+0j not in rock_coordinates2:
        landed = drop_sand(abyss_start, rock_coordinates2)
        sandcount2 += 1

    return sandcount, sandcount2


def drop_sand(abyss_start: int, rock_coordinates: set[complex]):
    current = 500 + 0j
    while current.imag != abyss_start + 2:
        if current + 1j not in rock_coordinates:
            current += 1j
            continue
        if current - 1 + 1j not in rock_coordinates:
            current += -1 + 1j
            continue
        if current + 1 + 1j not in rock_coordinates:
            current += 1 + 1j
            continue
        rock_coordinates.add(current)
        return True
    return False


def main(day):
    data = aocinput(day)
    result = overflow(data)
    print(result)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
