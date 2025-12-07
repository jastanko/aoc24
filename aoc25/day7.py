from collections import Counter

if __name__ == "__main__":

    with open(0) as data:
        start, *puzzle_input = data.read().splitlines()

    beams = Counter()
    beams[start.find("S")] = 1
    splits = 0

    for lines in puzzle_input:
        beams2 = beams.copy()
        for beam, count in beams.items():
            if lines[beam] == "^":
                splits += 1
                del beams2[beam]
                beams2[beam - 1] += count
                beams2[beam + 1] += count
        beams = beams2

    print(splits)
    print(beams.total())
