import os
from inputreader import aocinput
from typing import List, Tuple
from collections import deque
from functools import reduce


class Monkey:
    def __init__(self, definition: List[str], worry_reduction: int):
        self.items = deque([int(value) for value in definition[1].replace(',', '').split()[2:]])
        self.operation = eval(definition[2].replace('Operation: new =', 'lambda old: '))
        self.test = int(definition[3].split()[-1])
        self.true = int(definition[4].split()[-1])
        self.false = int(definition[5].split()[-1])
        self.inspected = 0
        self.worry_reduction = worry_reduction

    def throw(self, lcm: int) -> Tuple[int, int]:
        self.inspected += 1
        # results grow exponentially, keep remainder after modulo lcm since anything above lcm is not useful
        result = (self.operation(self.items.popleft()) // self.worry_reduction) % lcm
        if result % self.test:  # result not divisible
            return self.false, result
        else:
            return self.true, result

    def catch(self, value: int):
        self.items.append(value)


def monkey_business(data: List[str], worry_reduction, rounds) -> int:
    monkeys = [Monkey(data[i:i+7], worry_reduction) for i in range(0, len(data), 7)]
    lcm = reduce(lambda x, y: x * y, [monkey.test for monkey in monkeys])  # least common multiple, since all test integers seem prime

    for i in range(rounds):
        for monkey in monkeys:
            while monkey.items:
                to, value = monkey.throw(lcm)
                monkeys[to].catch(value)
    inspected = sorted([monkey.inspected for monkey in monkeys])[-2:]
    return inspected[-1] * inspected[-2]


def main(day):
    data = aocinput(day)
    result = monkey_business(data, 3, 20)
    result2 = monkey_business(data, 1, 10000)
    print(result, result2)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
