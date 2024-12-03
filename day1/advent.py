import pathlib
import sys


if __name__ == "__main__":

    input_file = pathlib.Path(__file__).parent.resolve().joinpath(sys.argv[1])
    with open(input_file, "r") as data:
        puzzle_input = data.read().splitlines()

    list0 = []
    list1 = []
    counts = dict()

    for line in puzzle_input:
        cols = line.split()
        list0.append(int(cols[0]))
        c1 = int(cols[1])
        list1.append(c1)
        if c1 in counts:
            counts[c1] += 1
        else:
            counts[c1] = 1

    list0.sort()
    list1.sort()
    total = 0
    similarity = 0
    for i in range(0, len(list0)):
        c0 = list0[i]
        total += abs(c0 - list1[i])
        if c0 in counts:
            similarity += c0*counts[c0]

    print(total)
    print(similarity)
