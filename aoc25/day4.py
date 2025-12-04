def remove_paper(grid):
    newgrid = []
    total = 0
    for y, row in enumerate(grid):
        newrow = []
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
                    newrow.append("x")
                else:
                    newrow.append("@")
            else:
                newrow.append(".")
        #         print(".", end="")
        newgrid.append(newrow)
        # print("")
    return newgrid, total


if __name__ == "__main__":

    with open(0) as data:
        puzzle_input = data.read()

    grid = puzzle_input.splitlines()
    total = 0
    while True:
        grid, removed = remove_paper(grid)
        total += removed
        if removed == 0:
            break

    # for row in newgrid:
    # print(row)
    print(total)
