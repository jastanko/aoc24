from collections import Counter


def num_paths(name, goal, devices, cache):
    if name == goal:
        return 1
    if name == "out":
        return 0
    if name in cache:
        return cache[name]
    sum = 0
    for out in devices[name]:
        sum += num_paths(out, goal, devices, cache)
    cache[name] = sum
    return sum


if __name__ == "__main__":

    with open(0) as data:
        puzzle_input = data.read().splitlines()

    devices = {}
    for line in puzzle_input:
        name, list = line.split(":")
        devices[name] = list.split()

    paths = (
        num_paths("svr", "fft", devices, Counter())
        * num_paths("fft", "dac", devices, Counter())
        * num_paths("dac", "out", devices, Counter())
    )
    paths += (
        num_paths("svr", "dac", devices, Counter())
        * num_paths("fft", "out", devices, Counter())
        * num_paths("dac", "fft", devices, Counter())
    )
    print(paths)
