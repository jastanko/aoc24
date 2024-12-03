import pathlib
import sys

def is_safe(levels):
    prev = int(levels.pop(0))
    min = 1
    max = 3
    if int(levels[0]) - prev < 0:
        min = -3
        max = -1
    for level in levels:
        delta = int(level) - prev
        if delta < min or delta > max:
            return False
        prev = int(level)
    return True

if __name__ == "__main__":

    input_file = pathlib.Path(__file__).parent.resolve().joinpath(sys.argv[1])
    with open(input_file, "r") as data:
        puzzle_input = data.read().splitlines()

    safe = 0
    for line in puzzle_input:
        if is_safe(line.split()):
            safe += 1

    print(safe)

    safe = 0
    for line in puzzle_input:
        if is_safe(line.split()):
            safe += 1
        else:
            levels = line.split()
            for i in range(0, len(levels)):
                levels = line.split()
                levels.pop(i)
                if is_safe(levels):
                    safe += 1
                    break

    print(safe)
