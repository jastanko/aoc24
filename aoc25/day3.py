if __name__ == "__main__":

    with open(0) as data:
        puzzle_input = data.read()

    total = 0
    for bank in puzzle_input.splitlines():
        bank.strip()
        b1 = b2 = 0
        for i in range(0, len(bank)-1):
            n = int(bank[i])
            if n > b1:
                b1 = n
                b2 = 0
            elif n > b2:
                b2 = n
            # print(f"{b1}{b2}")
        n = int(bank[-1])
        if n > b2:
            b2 = n
        joltage = b1*10 + b2
        # print(joltage)
        total += joltage

    print(total)
