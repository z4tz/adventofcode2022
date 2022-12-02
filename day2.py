import os
from inputreader import aocinput
from typing import List

translate = {'A': 0,
             'B': 1,
             'C': 2,
             'X': 0,
             'Y': 1,
             'Z': 2}


def gamescore(data: List[str]) -> int:
    score = 0
    for line in data:
        opponent, me = line.split()
        score += ((translate[me] - translate[opponent]) + 1) % 3 * 3 + (translate[me] + 1)  # result + shapevalue
    return score


def gamescore2(data: List[str]) -> int:
    score = 0
    for line in data:
        opponent, me = line.split()
        if me == 'X':
            score += (translate[opponent] - 1) % 3 + 1
        elif me == 'Y':
            score += (translate[opponent]) % 3 + 1 + 3
        else:
            score += (translate[opponent] + 1) % 3 + 1 + 6
    return score


def main(day):
    data = aocinput(day)
    result = gamescore(data)
    result2 = gamescore2(data)
    print(result, result2)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
