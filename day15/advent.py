import re
from collections import Counter

p = re.compile(r"p=(\d*),(\d*) v=(-?\d*),(-?\d*)")
WIDE = 101
TALL = 103
MID_X = (WIDE - 1) / 2
MID_Y = (TALL - 1) / 2
SECS = 100


def get_quadrant(line):
    robot = p.match(line)
    x = (int(robot[1]) + int(robot[3]) * SECS) % WIDE
    y = (int(robot[2]) + int(robot[4]) * SECS) % TALL
    # print(f"{x},{y}")
    if x < MID_X:
        if y < MID_Y:
            return "A"
        elif y > MID_Y:
            return "C"
    elif x > MID_X:
        if y < MID_Y:
            return "B"
        elif y > MID_Y:
            return "D"
    return "_"


if __name__ == "__main__":

    with open(0) as data:
        puzzle_input = data.read()

    dirs = {"<": (-1, 0), "^": (0, -1), ">": (1, 0), "v": (0, 1)}

    warehouse = []
    robot = (0,0)
    for y, line in enumerate(puzzle_input.splitlines()):
        loc = line.find("@")
        if loc != -1:
            robot = (loc, y)
        warehouse.append(list(line))

    print(warehouse[robot[1]])
    print(robot)
