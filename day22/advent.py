PRUNE = 16777216

def pseudorandom(x):
    for i in range(2000):
        x = (x * 64 ^ x) % PRUNE
        x = (x // 32 ^ x) % PRUNE
        x = (x * 2048 ^ x) % PRUNE
    return x

if __name__ == "__main__":

    with open(0) as data:
        puzzle_input = data.read().splitlines()

    print(sum(map(pseudorandom, map(int, puzzle_input))))
