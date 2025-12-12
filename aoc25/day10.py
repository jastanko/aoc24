from collections import deque


def min_presses(lights, buttons):
    queue = deque((b, 1) for b in buttons)

    while queue:
        # for _ in range(100000):
        node, count = queue.popleft()
        if node == lights:
            return count
        # print(node, end=" ")
        queue.extend((node ^ n, count + 1) for n in buttons)

    raise Exception("exceeded max range")


def get_toggles(buttons):
    toggles = 0
    for button in buttons:
        toggles += 2 ** int(button)
    return toggles


if __name__ == "__main__":

    with open(0) as data:
        puzzle_input = data.read().splitlines()

    total = 0
    for line in puzzle_input:
        machine = line.split()

        lights = 0
        for light in machine[0][-1:0:-1]:
            lights *= 2
            if light == "#":
                lights += 1

        toggles = []
        for blist in machine[1:-1]:
            buttons = [int(n) for n in blist[1:-1].split(",")]
            toggles.append(get_toggles(buttons))

        print(f"{lights:b} {toggles} {total}")
        total += min_presses(lights, toggles)

    print(total)
