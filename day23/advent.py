from collections import defaultdict

if __name__ == "__main__":

    with open(0) as data:
        puzzle_input = data.read().splitlines()

    cons = defaultdict(set)

    for pair in puzzle_input:
        a, b = pair.split("-")
        cons[a].add(b)
        cons[b].add(a)

    parties = {
        str(sorted([k, b, c]))
        for k, v in cons.items()
        if k.startswith("t")
        for b in v
        for c in v
        if b != c and b in cons[c]
    }
    print(len(parties))
