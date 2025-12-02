if __name__ == "__main__":

    with open(0) as data:
        puzzle_input = data.read().splitlines()

    dial = 50
    pw = 0
    for rot in puzzle_input:
        delta = int(rot[1:])
        factor = 1
        if rot[0] == "L":
            factor = -1
        dialp = dial + delta*factor
        clicks = abs(dialp//100)
        if dial == 0 and factor == -1 and clicks > 0:
            clicks -= 1
        dial = dialp % 100
        if dial == 0 and factor == -1:
            pw += 1
        pw += clicks
        # print(f"dial: {dial} clicks: {pw}")

    print(f"password: {pw}")
