import os
from inputreader import aocinput
from typing import List, Tuple


def signal_sum(data: List[str]) -> Tuple[int, str]:
    register = 1
    history = [1]
    for line in data:
        if line.startswith('a'):
            history.append(register)  # add previous value once for first cycle
            register += int(line[4:])
            history.append(register)
        else:
            history.append(register)

    screen = []
    for i, value in enumerate(history):
        if abs(value - i % 40) <= 1:
            screen.append('##')
        else:
            screen.append('  ')

    return sum([i * history[i-1] for i in [20, 60, 100, 140, 180, 220]]), '\n'.join([''.join(screen[i:i+40]) for i in range(0,len(screen), 40)])


def main(day):
    data = aocinput(day)
    result, result2 = signal_sum(data)
    print(result)
    print(result2)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
