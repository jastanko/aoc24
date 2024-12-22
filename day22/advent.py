from collections import Counter

PRUNE = 16777216
CYCLES = 2000
BANANA_DICT = Counter()

def pseudorandom(x):
    prices = [x % 10]
    for i in range(CYCLES):
        x = (x * 64 ^ x) % PRUNE
        x = (x // 32 ^ x) % PRUNE
        x = (x * 2048 ^ x) % PRUNE
        prices.append(x % 10)

    deltas = [y - x for x, y in zip(prices[:-1], prices[1:])]
    seq_dict = dict()
    for i in range(4, len(prices)):
        seq = str(deltas[i-4:i])
        if not seq in seq_dict:
            seq_dict[seq] = prices[i]

    for k, v in seq_dict.items():
        BANANA_DICT[k] += v
    return x

if __name__ == "__main__":

    with open(0) as data:
        puzzle_input = data.read().splitlines()

    print(sum(map(pseudorandom, map(int, puzzle_input))))

    bananas = max(BANANA_DICT, key=BANANA_DICT.get)
    print(bananas)
    print(BANANA_DICT[bananas])

