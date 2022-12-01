import os
from inputreader import aocinput
from typing import List


def count_calories(calorie_count: List[str]) -> int:
    max_calories = 0
    current_calories = 0
    for line in calorie_count:
        if line.strip().isnumeric():
            current_calories += int(line)
        else:
            max_calories = max([current_calories, max_calories])
            current_calories = 0
    return max_calories


def count_top_calories(calorie_count: List[str]) -> int:
    calories = []
    current_calories = 0
    for line in calorie_count:
        if line.strip().isnumeric():
            current_calories += int(line)
        else:
            calories.append(current_calories)
            current_calories = 0
    return sum(sorted(calories, reverse=True)[:3])


def main(day):
    data = aocinput(day)
    result = count_calories(data)
    result2 = count_top_calories(data)
    print(result, result2)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
