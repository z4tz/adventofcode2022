import os
from inputreader import aocinput
import numpy as np
from itertools import cycle
from collections import deque


class Rock:
    shapes = {0: [2, 3, 4, 5],
              1: [3, 2 + 1j, 3 + 1j, 4 + 1j, 3 + 2j],
              2: [2, 3, 4, 4 + 1j, 4 + 2j],
              3: [2, 2 + 1j, 2 + 2j, 2 + 3j],
              4: [2, 3, 2 + 1j, 3 + 1j]}

    def __init__(self, shape_index, start_height):
        self._shape_index = shape_index
        self._height = complex(0, start_height)
        self._x_coord = 0

    def get_coords(self, x_change=0, drop=0) -> list[complex]:
        return [number + self._x_coord + x_change + self._height + complex(0, drop) for number in self.shapes[self._shape_index]]

    def fall(self):
        self._height -= 1j

    def move(self, direction):
        self._x_coord += direction


def display(rocks: set[complex], moving_rock: Rock = None) -> None:
    try:
        max_imag = max(rocks, key=lambda x: x.imag).imag
    except ValueError:
        max_imag = 0
    arr = np.full([int(max_imag) + 8, 7], '.', dtype='str')

    for rock in rocks:
        arr[int(rock.imag), int(rock.real)] = '#'

    if moving_rock:
        for coord in moving_rock.get_coords():
            arr[int(coord.imag), int(coord.real)] = '@'

    arr = np.flipud(arr)
    for row in arr:
        string = ' '.join(row)
        print(f'|{string}|')
    print('---------------')


def tower_height(data: str, released_rocks) -> int:
    directions = cycle(enumerate([1 if char == '>' else -1 for char in data]))
    spawn_height = 3
    solid_rocks = set()
    tracked = {}
    for i in range(released_rocks):
        rock = Rock(i % 5, spawn_height)
        while True:
            direction_count, direction = next(directions)
            if i > 1000:
                key = (i % 5, direction_count)
                if key in tracked:
                    prev_i, prev_height = tracked[key]
                    period = i - prev_i
                    if i % period == released_rocks % period:
                        period_height = spawn_height - prev_height
                        periods_remaining = (released_rocks - i) // period

                        total_height = spawn_height - 3 + (period_height * periods_remaining)
                        return int(total_height)

                else:
                    tracked[key] = (i, spawn_height)

            coord_move = rock.get_coords(x_change=direction)
            if not any([coord in solid_rocks or coord.real >= 7 or coord.real <= -1 for coord in coord_move]):
                rock.move(direction)

            coord_fall = rock.get_coords(drop=-1)
            if not any([coord in solid_rocks or coord.imag == -1 for coord in coord_fall]):
                rock.fall()
            else:
                spawn_height = max([max(rock.get_coords(), key=lambda x: x.imag).imag + 4, spawn_height])   # new spawn height 3 above highest, if its higher than previous
                solid_rocks.update(rock.get_coords())
                break

    return int(max(rock.get_coords(), key=lambda x: x.imag).imag) + 1


def main(day):
    data = aocinput(day)

    result = tower_height(data[0], 2022)
    result2 = tower_height(data[0], 1000000000000)

    print(result)
    print(result2)

if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
