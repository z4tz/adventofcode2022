from typing import List


def aocinput(day: int) -> List[str]:
    with open(f'inputs/day{day}.txt') as f:
        lines = f.readlines()
    return lines