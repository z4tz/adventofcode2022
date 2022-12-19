import os
from inputreader import aocinput
import re
from dataclasses import dataclass
from itertools import permutations

@dataclass
class Valve:
    name: str
    flow_rate: int
    access_names: list
    access_times: dict = None


results = []
results2 = []


def release_pressure(data: list[str]) -> int:
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

    def action(valve: Valve, time_remaining: int, pressure: int, closed_valves: set[str]):
        if time_remaining <= 0 or len(closed_valves) == 0:
            results.append(pressure)
            return
        for next_valve in closed_valves:
            new_closed = closed_valves.copy()
            new_closed.remove(next_valve)
            action(valves[next_valve], time_remaining - valve.access_times[next_valve], pressure + valves[next_valve].flow_rate * (time_remaining-valve.access_times[next_valve]), new_closed)

    def elephant_action(valve1, valve2, time1: int, time2: int, pressure: int, closed_valves: set[str]):
        if len(closed_valves) == 0 or (time1 <=0 and time2 <= 0):
            #print(time1, time2)
            results2.append(pressure)
            return
        elif len(closed_valves) == 1:
            next_valve = closed_valves.pop()
            pressure_1 = valves[next_valve].flow_rate * (time1-valve1.access_times[next_valve])
            pressure_2 = valves[next_valve].flow_rate * (time2-valve2.access_times[next_valve])
            if pressure_1 > pressure_2:
                elephant_action(valves[next_valve], valve2, time1 - valve1.access_times[next_valve], time2, pressure + pressure_1, set())
            else:
                elephant_action(valve1, valves[next_valve], time1, time2 - valve2.access_times[next_valve], pressure + pressure_2, set())
        else:
            for next1, next2 in permutations(closed_valves, 2):
                if time1-valve1.access_times[next1] < 0 or time2-valve2.access_times[next2] < 0:
                    continue
                new_closed = closed_valves.copy()
                new_closed.remove(next1)
                new_closed.remove(next2)
                new_pressure = pressure + valves[next1].flow_rate * (time1-valve1.access_times[next1])
                new_pressure = new_pressure + valves[next2].flow_rate * (time2-valve2.access_times[next2])
                elephant_action(valves[next1], valves[next2], time1 - valve1.access_times[next1], time2 - valve2.access_times[next2], new_pressure,new_closed)




    relevant_closed_valves = [valve for valve in valves.keys() if valves[valve].flow_rate>0]
    #action(valves['AA'], 30, 0, set(relevant_closed_valves))
    #print(max(results))
    elephant_action(valves['AA'], valves['AA'], 26, 26, 0, set(relevant_closed_valves))
    print(max(results2))



def main(day):
    data = aocinput(day)
    result = release_pressure(data)
    print(result)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
