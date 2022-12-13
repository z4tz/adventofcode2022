import os
from inputreader import aocinput
from typing import List, Tuple, Union
from itertools import zip_longest
from functools import cmp_to_key


def validate(a: List[Union[List, int]], b: List[Union[List, int]]):
    result = 0
    for left, right in zip_longest(a, b):
        if left is None:
            return -1
        elif right is None:
            return 1
        elif type(left) is int and type(right) is int:
            if left < right:
                return -1
            elif right < left:
                return 1
        elif type(left) == type(right):  # both are lists
            result = validate(left, right)
        elif type(left) is list:
            result = validate(left, [right])
        else:
            result = validate([left], right)
        if result:
            return result


def flatten(xs):
    for x in xs:
        if type(x) is list:
            yield from flatten(x)
        else:
            yield x


def valid_pairs(data: List[str]) -> Tuple[int, int]:
    valid = 0
    lists = [[2], [6]]
    for i in range(0, len(data), 3):
        lists.append(row1 := eval(data[i]))
        lists.append(row2 := eval(data[i+1]))
        if validate(row1, row2) < 0:
            valid += i//3 + 1
    lists.sort(key=cmp_to_key(validate))
    return valid, (lists.index([2]) + 1) * (lists.index([6]) + 1)


def main(day):
    data = aocinput(day)
    result = valid_pairs(data)
    print(result)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
