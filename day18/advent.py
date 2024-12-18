import copy

MEM_MAX = 70
READ_BYTES = 1024


def shortest_path(mem):
    mem_space = copy.deepcopy(mem)
    next_steps = [(0, 0)]
    steps = 0
    while len(next_steps) > 0:
        next = []
        for x, y in next_steps:
            if x == MEM_MAX and y == MEM_MAX:
                return steps
            if mem_space[y][x] == ".":
                if x < MEM_MAX:
                    next.append((x + 1, y))
                if x > 0:
                    next.append((x - 1, y))
                if y < MEM_MAX:
                    next.append((x, y + 1))
                if y > 0:
                    next.append((x, y - 1))
                mem_space[y][x] = "O"
        next_steps = next
        steps += 1
    return -1


if __name__ == "__main__":

    with open(0) as data:
        puzzle_input = data.read().splitlines()

    mem_space = [["." for _ in range(MEM_MAX + 1)] for _ in range(MEM_MAX + 1)]
    for i in range(READ_BYTES):
        x, y = puzzle_input[i].split(",")
        mem_space[int(y)][int(x)] = "#"

    print(shortest_path(mem_space))
    for i in range(READ_BYTES, len(puzzle_input)):
        x, y = puzzle_input[i].split(",")
        mem_space[int(y)][int(x)] = "#"
        if shortest_path(mem_space) == -1:
            print(puzzle_input[i])
            break
