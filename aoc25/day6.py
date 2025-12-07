import math

if __name__ == "__main__":

    with open(0) as data:
        puzzle_input = data.read().splitlines()

    symbols = puzzle_input.pop().split(" ")
    symbols = list(filter(lambda c: len(c) > 0, symbols))

    matrix = list()
    numlist = list()
    # for line in puzzle_input:
    # matrix.append(list(map(int, filter(lambda c: len(c) > 0, line.split(" ")))))
    for col in range(0, len(puzzle_input[0])):
        snum = ""
        for line in puzzle_input:
            snum += line[col]
        snum = snum.strip()
        if len(snum) > 0:
            numlist.append(int(snum))
            # print(f"list={numlist}")
        else:
            matrix.append(numlist)
            numlist = list()
            # print(matrix)

    matrix.append(numlist)

    # print(matrix)
    cols = matrix
    # cols = list(zip(*matrix))
    total = 0
    for i, symbol in enumerate(symbols):
        if symbol == "+":
            total += sum(cols[i])
        elif symbol == "*":
            total += math.prod(cols[i])

    print(total)
