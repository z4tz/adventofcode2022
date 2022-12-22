import os
from inputreader import aocinput


class Number:
    def __init__(self, value):
        self.value: int = value

    def __repr__(self):
        return str(self.value)


def coord_sum(data: list[str], key=1, rounds=1) -> int:

    zero = None
    new_data = []
    for line in data:
        if int(line) == 0:
            zero = Number(0)
            new_data.append(zero)
        else:
            new_data.append(Number(int(line)*key))
    data = new_data
    datalength = len(data)
    datacopy = data[:]
    for _ in range(rounds):
        for number in datacopy:
            old_index = data.index(number)
            new_index = (old_index + number.value) % (datalength-1)
            data.remove(number)

            data.insert(new_index, number)

    zero_index = data.index(zero)

    return sum(data[(zero_index+num) % datalength].value for num in [1000, 2000, 3000])


def main(day):
    data = aocinput(day)
    result = coord_sum(data)
    result2 = coord_sum(data, 811589153, 10)

    print(result, result2)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
