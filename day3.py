import os
import string
from inputreader import aocinput
from typing import List, Iterable


def duplicate(characters: str, to_compare: str) -> str:
    for char in characters:
        if char in to_compare:
            return char


def duplicates(characters: Iterable, to_compare: Iterable) -> Iterable:
    return [char for char in characters if char in to_compare]


def get_priority(char: str) -> int:
    return string.ascii_letters.index(char) + 1


def itempriority(data: List[str]) -> int:
    return sum(get_priority(duplicate(line[int(len(line) / 2):], line[:int(len(line) / 2)])) for line in data)


def badgepriority(data: List[str]) -> int:
    priority_sum = 0
    for elves in [data[i:i+3] for i in range(0, len(data), 3)]:
        priority_sum += get_priority(duplicates(duplicates(elves[0], elves[1]), elves[2])[0])
    return priority_sum


def main(day):
    data = aocinput(day)
    result = itempriority(data)
    result2 = badgepriority(data)

    print(result, result2)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
