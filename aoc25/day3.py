NUM_BATTERIES = 12

if __name__ == "__main__":

    with open(0) as data:
        puzzle_input = data.read()

    total = 0
    for bank in puzzle_input.splitlines():
        bank.strip()
        jlt = []
        for i in range(0, len(bank)):
            n = int(bank[i])
            minl = max(0, NUM_BATTERIES + i - len(bank))
            while len(jlt) > minl and jlt[-1] < n:
                jlt.pop()
            jlt.append(n)
        
        while len(jlt) > NUM_BATTERIES:
            jlt.pop()

        # print(jlt)
        n = int(bank[-1])
        joltage = 0
        place = 1
        while len(jlt) > 0:
            joltage += jlt.pop() * place
            place *= 10
        # print(joltage)
        total += joltage

    print(total)
