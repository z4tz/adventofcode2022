import os
from inputreader import aocinput
from itertools import product


# remake solution, have a function that takes a machine state and produces all possible states
# then put all states in queue and work through them

def blueprint_quality(data: list[str]) -> int:
    blueprints = []
    for line in data:
        parts = line.split()
        blueprints.append(
            (int(parts[6]), int(parts[12]), (int(parts[18]), int(parts[21])), (int(parts[27]), int(parts[30]))))
    geode_count = []
    for blueprint in blueprints:
        time = 24
        mine_geode(blueprint, [1, 4, 2, 2], 24)
        print('------------')
        # geode_count.append(max([mine_geode(blueprint, robot_max, time) for robot_max in product([1,2,3,4,5,6], repeat=4)]))

    print(geode_count)


def mine_geode(blueprint, robot_max, time):
    robots = [1, 0, 0, 0]
    resources = [0, 0, 0, 0]
    # robot_max = [2, 4, 3, 5]
    for t in range(time):

        # build new robots
        new_robots = [0, 0, 0, 0]

        if robots[0] < robot_max[0] and resources[0] >= blueprint[0]:
            new_robots[0] += 1
            resources[0] -= blueprint[0]

        if resources[0] >= blueprint[3][0] and resources[2] >= blueprint[3][1]:
            new_robots[3] += 1
            resources[0] -= blueprint[3][0]
            resources[2] -= blueprint[3][1]

        if robots[1] < robot_max[1] and resources[0] >= blueprint[1]:
            new_robots[1] += 1
            resources[0] -= blueprint[1]

        if robots[2] < robot_max[2] and resources[0] >= blueprint[2][0] and resources[1] >= blueprint[2][1]:
            new_robots[2] += 1
            resources[0] -= blueprint[2][0]
            resources[1] -= blueprint[2][1]

        # add material
        for material in range(4):
            resources[material] += robots[material]

        print(t+1, robots, resources, new_robots)

        for i, new_robot in enumerate(new_robots):
            robots[i] += new_robot

    return resources[3]


def main(day):
    data = aocinput(day)
    result = blueprint_quality(data)
    print(result)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
