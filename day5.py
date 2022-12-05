import os
from inputreader import aocinput
from typing import List, Tuple
from collections import deque


def stacked_crates(data: List[str]) -> Tuple[str, str]:
    linebreak = data.index('\n')  # get break between stack-info and move-info

    # create stacks
    stack_count = int(data[linebreak-1].split()[-1])
    stacks = [deque() for i in range(stack_count)]
    stacks2 = [deque() for i in range(stack_count)]  # part 2
    for line in reversed(data[:stack_count-1]):  # reverse to build stacks from bottom and up
        for i in range(stack_count):
            value = line[i * 4 + 1]
            if value != ' ':
                stacks[i].append(value)
                stacks2[i].append(value)

    for line in data[stack_count+1:]:
        _, count, _, from_stack, _, to_stack = line.split()
        tempstack = deque()  # part 2
        for i in range(int(count)):
            stacks[int(to_stack)-1].append(stacks[int(from_stack)-1].pop())
            tempstack.appendleft(stacks2[int(from_stack)-1].pop())
        stacks2[int(to_stack)-1].extend(tempstack)

    return ''.join([stack.pop() for stack in stacks]), ''.join([stack.pop() for stack in stacks2])


def main(day):
    data = aocinput(day)
    result = stacked_crates(data)
    print(result)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
