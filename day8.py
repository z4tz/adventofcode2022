import os
from inputreader import aocinput
from typing import List
import numpy as np


def visible_trees(data: List[str]):
    treeheights = np.array([[int(char) for char in line.strip()] for line in data])
    visible = np.ones(treeheights.shape, dtype=int)
    visible[1:-1, 1:-1] = 0  # all edges already visible
    scenic_score = np.ones(treeheights.shape, dtype=int)
    for rotations in range(4):
        for y in range(1, treeheights.shape[1]-1):
            rowmax = treeheights[y, 0]
            for x in range(1, treeheights.shape[0]-1):
                # part 1
                if treeheights[y, x] > rowmax:
                    rowmax = treeheights[y, x]
                    visible[y, x] = 1

                # part 2
                start_height = treeheights[y, x]
                i = 1
                while x + i < treeheights.shape[0] - 1 and start_height > treeheights[y, x + i]:
                    i += 1
                scenic_score[y, x] *= i

        if rotations < 3:  # skip last rotation
            treeheights = np.rot90(treeheights)
            visible = np.rot90(visible)
            scenic_score = np.rot90(scenic_score)
    return np.sum(visible), np.max(scenic_score)


def main(day):
    data = aocinput(day)
    result = visible_trees(data)
    print(result)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
