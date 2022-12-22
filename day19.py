import os
from inputreader import aocinput
import math


def blueprint_quality(data: list[str], total_time) -> tuple[int, int]:
    blueprints = []
    for line in data:
        parts = line.split()
        blueprints.append(
            (int(parts[6]), int(parts[12]), (int(parts[18]), int(parts[21])), (int(parts[27]), int(parts[30]))))
    geode_counts = []
    for blueprint in blueprints:
        max_needed = [max([blueprint[0], blueprint[1], blueprint[2][0], blueprint[3][0]]), blueprint[2][1],
                      blueprint[3][1]]

        seen_states = set()
        states = {((1, 0, 0, 0), (0, 0, 0, 0))}

        for time in range(total_time):
            new_states = set()
            best_state = ((1, 0, 0, 0), (0, 0, 0, 0))
            while states:
                for state in process_state(blueprint, states.pop(), max_needed):
                    if state[1][3] + 5 > best_state[1][3] and state[0][3] + 2 > best_state[0][3]:
                        if state not in seen_states:
                            if state[1][3] > best_state[1][3]:
                                best_state = state
                            new_states.add(state)
                    seen_states.add(state)
            states = new_states

        best_state = max(new_states, key=lambda x: x[1][3])
        geode_counts.append(best_state[1][3])

    return sum([(i + 1) * count for i, count in enumerate(geode_counts)]), math.prod(geode_counts)


def process_state(blueprint, state: tuple[tuple, tuple], max_robots) -> list[tuple[tuple, tuple]]:
    (robots, resources) = state
    new_resources = add_tuples(resources, robots)

    new_states = []  # include state where no robot was purchased

    if resources[0] >= blueprint[3][0] and resources[2] >= blueprint[3][1]:
        new_states.append(
            (add_tuples(robots, (0, 0, 0, 1)), add_tuples(new_resources, (-blueprint[3][0], 0, -blueprint[3][1], 0))))
        return new_states

    if resources[0] >= blueprint[0] and robots[0] < max_robots[0]:
        new_states.append((add_tuples(robots, (1, 0, 0, 0)), add_tuples(new_resources, (-blueprint[0], 0, 0, 0))))

    if resources[0] >= blueprint[1] and robots[1] < max_robots[1]:
        new_states.append((add_tuples(robots, (0, 1, 0, 0)), add_tuples(new_resources, (-blueprint[1], 0, 0, 0))))

    if resources[0] >= blueprint[2][0] and resources[1] >= blueprint[2][1] and robots[2] < max_robots[2]:
        new_states.append(
            (add_tuples(robots, (0, 0, 1, 0)), add_tuples(new_resources, (-blueprint[2][0], -blueprint[2][1], 0, 0))))

    new_states.append((robots, new_resources))

    return new_states


def add_tuples(tuple1, tuple2):
    return tuple(a + b for a, b in zip(tuple1, tuple2))


def main(day):
    data = aocinput(day)
    result = blueprint_quality(data, 24)[0]
    result2 = blueprint_quality(data[:3], 32)[1]
    print(result, result2)
    #print(result2)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
