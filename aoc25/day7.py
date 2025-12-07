if __name__ == "__main__":

    with open(0) as data:
        start, *puzzle_input = data.read().splitlines()

    beams = set()
    beams.add(start.find("S"))
    splits = 0

    for lines in puzzle_input:
        beams2 = beams.copy()
        for beam in beams:
            if lines[beam] == "^":
                splits += 1
                beams2.remove(beam)
                beams2.add(beam - 1)
                beams2.add(beam + 1)
        beams = beams2

    print(splits)
