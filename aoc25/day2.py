def valid(id: str) -> int:
    mid = len(id) // 2
    if id[mid:] == id[:mid]:
        return int(id)
    return 0


def repeats(id):
    # print(f"checking:{id} len={len(id)}")
    for step in range(1, len(id)):
        # print(step)
        if (len(id) % step) == 0:
            pattern = id[0:step]
            # print(f"pattern: {pattern}")
            repeats = True
            for i in range(step, len(id), step):
                if pattern != id[i : i + step]:
                    # print(f"no match at step {step}")
                    repeats = False
                    break
            if repeats:
                # print(f"invalid id: {id}")
                return int(id)
    return 0


if __name__ == "__main__":

    with open(0) as data:
        puzzle_input = data.read().strip()

    total = 0
    for pair in puzzle_input.split(","):
        ids = pair.split("-")
        for id in range(int(ids[0]), int(ids[1]) + 1):
            total += valid(str(id))

    print(total)
