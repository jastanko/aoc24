def blink(stone, count):
    if count == 0:
        return 1

    if stone == 0:
        return blink(1, count-1)

    str_stone = str(stone)
    if len(str_stone)%2 == 0:
        mid = int(len(str_stone)/2)
        return blink(int(str_stone[:mid]), count-1) + blink(int(str_stone[mid:]), count-1)

    return blink(int(stone)*2024, count-1)

if __name__ == "__main__":

    stones = map(int, open(0).read().split())

    total = 0
    for stone in stones:
        total += blink(stone, 75)

    print(total)
