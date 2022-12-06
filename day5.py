import os
from inputreader import aocinput
from typing import List, Tuple
from collections import deque


def stacked_crates(data: List[str]) -> Tuple[str, str]:
    linebreak = data.index('\n')  # get break between stack-info and move-info

    # create stacks
    stack_count = int(data[linebreak-1].split()[-1])
    stacks = [list() for i in range(stack_count)]
    stacks2 = [list() for i in range(stack_count)]  # part 2
    for line in reversed(data[:linebreak-1]):  # reverse to build stacks from bottom and up
        for i in range(stack_count):
            value = line[i * 4 + 1]
            if value != ' ':
                stacks[i].append(value)
                stacks2[i].append(value)

    for line in data[linebreak+1:]:
        _, count, _, from_stack, _, to_stack = line.split()
        count = int(count)
        from_stack = int(from_stack)
        to_stack = int(to_stack)
        stacks[to_stack - 1].extend(reversed(stacks[from_stack-1][-count:]))
        del stacks[from_stack - 1][-count:]
        stacks2[to_stack - 1].extend(stacks2[from_stack - 1][-count:])
        del stacks2[from_stack - 1][-count:]

    return ''.join([stack.pop() for stack in stacks]), ''.join([stack.pop() for stack in stacks2])


def main(day):
    data = aocinput(day)
    result = stacked_crates(data)
    print(result)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
