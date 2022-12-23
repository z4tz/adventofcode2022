import os
from inputreader import aocinput


def number_yelling(data: list[str]) -> int:
    monkeys = {}
    for line in data:
        parts = line.strip().split(': ')
        if parts[1].isnumeric():
            monkeys[parts[0]] = eval(f'lambda x: {int(parts[1])}')
        else:
            subparts = parts[1].split()
            monkeys[parts[0]] = eval(f'lambda x : x[\'{subparts[0]}\'](x) {subparts[1]} x[\'{subparts[2]}\'](x)')
    return int(monkeys['root'](monkeys))


def number_yelling2(data: list[str], humn: str) -> int:
    monkeys = {}
    for line in data:
        parts = line.strip().split(': ')
        if parts[0] == 'humn':
            parts[1] = humn

        if parts[1].isnumeric():
            monkeys[parts[0]] = eval(f'lambda x: {int(parts[1])}')
        else:
            subparts = parts[1].split()
            if parts[0] == 'root':
                subparts[1] = '-'

            monkeys[parts[0]] = eval(f'lambda x : x[\'{subparts[0]}\'](x) {subparts[1]} x[\'{subparts[2]}\'](x)')
    return monkeys['root'](monkeys)


def find_humn_number(data: list[str]) -> int:
    # To find where roots numbers are equal put roots calculation to subtraction -> answer should be zero
    # Check how much answer varies with two inputs and use it to calculate value humn should yell
    
    number = 1000000000000  # use large number to not have rounding affect the calculation?
    probe1 = number_yelling2(data, '0')
    probe2 = number_yelling2(data, f'{number}')
    return int(-probe1/(probe2 - probe1)*number)


def main(day):
    data = aocinput(day)
    result = number_yelling(data)
    result2 = find_humn_number(data)
    print(result, result2)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
