DESIGN_DICT = dict()


def possible(towels, design):
    if len(design) == 0:
        return 1
    if design in DESIGN_DICT:
        return DESIGN_DICT[design]
    count = 0
    for towel in towels:
        if design.startswith(towel):
            count += possible(towels, design[len(towel) :])
    DESIGN_DICT[design] = count
    return count


if __name__ == "__main__":

    with open(0) as data:
        puzzle_input = data.read().splitlines()

    towels = [s.strip() for s in puzzle_input[0].split(",")]

    poss = [possible(towels, design) for design in puzzle_input[2:]]
    print(sum(poss))
