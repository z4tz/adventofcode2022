import os
from collections import defaultdict
from inputreader import aocinput
import re
from dataclasses import dataclass


@dataclass
class Valve:
    name: str
    flow_rate: int
    access_names: list
    access_times: dict = None


def release_pressure(data: list[str]) -> tuple[int, int]:
    valves = {}
    regex = re.compile(r"^Valve (..) has flow rate=(\d*); tunnels* leads* to valves* ([A-Z, ]*)$")
    for line in data:
        groups = regex.match(line).groups()
        valves[groups[0]] = Valve(groups[0], int(groups[1]), groups[2].split(', '))

    for valve_name in valves.keys():
        shortest = {valve_name: 1}
        steps = 2
        current = {valve_name}
        visited = {valve_name}
        while current:
            next_visit = set()
            for name in current:
                for next_valve in valves[name].access_names:
                    if next_valve not in visited:
                        visited.add(next_valve)
                        shortest[next_valve] = steps
                        next_visit.add(next_valve)
            current = next_visit
            steps += 1
        valves[valve_name].access_times = shortest

    relevant_closed_valves = [valve for valve in valves.keys() if valves[valve].flow_rate > 0]

    def action(valve: Valve, time_remaining: int, pressure: int, closed_valves: set[str], open_valves: frozenset[str]):
        states[open_valves] = max([pressure, states[open_valves]])
        for next_valve in closed_valves:
            new_time = time_remaining - valve.access_times[next_valve]
            if new_time >= 0:
                new_closed = closed_valves.copy()
                new_closed.remove(next_valve)
                new_open = frozenset([*open_valves, next_valve])
                action(valves[next_valve], new_time, pressure + valves[next_valve].flow_rate * new_time, new_closed, new_open)
    # part 1
    states = defaultdict(int)
    action(valves['AA'], 30, 0, set(relevant_closed_valves), frozenset())
    result = max(states.values())

    # part 2
    states = defaultdict(int)
    action(valves['AA'], 26, 0, set(relevant_closed_valves), frozenset())
    max_score = 0
    for state1 in states.items():  # find the two states with max score that didn't open the same valve
        for state2 in states.items():
            if (score := state1[1] + state2[1]) > max_score and state1[0].isdisjoint(state2[0]):
                max_score = score

    return result, max_score


def main(day):
    data = aocinput(day)
    result = release_pressure(data)
    print(result)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
