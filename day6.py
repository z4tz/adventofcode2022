import os
from inputreader import aocinput
from collections import deque


def find_marker(datastream: str, markerlength=4) -> int:
    buffer = deque(datastream[:markerlength], maxlen=markerlength)
    for i in range(markerlength, len(datastream)):
        if len(set(buffer)) == markerlength:
            return i
        buffer.append(datastream[i])


def main(day):
    data = aocinput(day)
    result = find_marker(data[0], 4)
    result2 = find_marker(data[0], 14)
    print(result, result2)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
