import os
import re
from inputreader import aocinput
from typing import List, Tuple


def covered_ranges(data: List[str]) -> Tuple[int, int]:
    covered_count = 0
    any_overlap = 0
    for line in data:
        parts = [int(char) for char in re.split(',|-', line.strip())]
        if parts[0] <= parts[2] and parts[1] >= parts[3] or parts[2] <= parts[0] and parts[3] >= parts[1]:
            covered_count += 1
        if parts[3] >= parts[0] >= parts[2] or parts[3] >= parts[1] >= parts[2] or parts[1] >= parts[2] >= parts[0] or parts[1] >= parts[3] >= parts[0]:
            any_overlap += 1

    return covered_count, any_overlap


def main(day):
    data = aocinput(day)
    result = covered_ranges(data)
    print(result)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
