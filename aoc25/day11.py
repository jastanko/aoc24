def num_paths(name, devices):
    if devices[name][0] == "out":
        return 1
    sum = 0
    for out in devices[name]:
        sum += num_paths(out, devices)
    return sum


if __name__ == "__main__":

    with open(0) as data:
        puzzle_input = data.read().splitlines()

    devices = {}
    for line in puzzle_input:
        name, list = line.split(":")
        devices[name] = list.split()

    print(num_paths("you", devices))
