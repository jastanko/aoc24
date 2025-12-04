if __name__ == "__main__":

    with open(0) as data:
        puzzle_input = data.read()

    grid = puzzle_input.splitlines()
    total = 0
    for y, row in enumerate(grid):
        for x, roll in enumerate(row):
            if roll == "@":
                count = 0
                for xd in range(max(0, x - 1), min(x + 2, len(row))):
                    for yd in range(max(0, y - 1), min(y + 2, len(grid))):
                        pos = grid[yd][xd]
                        # print(f"{xd},{yd}:{pos}")
                        if pos == "@":
                            count += 1
                # print(count, end="")
                if count <= 4:
                    total += 1
        #     else:
        #         print(".", end="")
        # print("")

    print(total)
