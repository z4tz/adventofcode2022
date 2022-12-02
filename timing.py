import timeit
import os
import sys


def setupstring(day):
    return f"""
from day{day} import main"""


def time_day(day, mintime=1):
    print("-----## Assignment day {0} ##-----".format(day))
    runs = 1
    time = timeit.timeit(f"main({day})", setup=setupstring(day), number=1)
    sys.stdout = open(os.devnull, 'w')  # disable print statements
    while time < mintime:
        runs += 1
        time += timeit.timeit(f"main({day})", setup=setupstring(day), number=1)

    sys.stdout = sys.__stdout__  # enable print statements again
    print(f"Time used for assignment {day}: {time/runs:.5f}s - average over {runs} run{'' if runs == 1 else 's'}\n\n")


def main():
    days = range(1, len(os.listdir('inputs/')) + 1)

    for day in days:
        time_day(day, 1)


if __name__ == '__main__':
    main()