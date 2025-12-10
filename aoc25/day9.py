def area(points):
    point1, point2 = points

    return (abs(point2[0] - point1[0]) + 1) * (abs(point2[1] - point1[1]) + 1)


def is_red_green(p1, p2, boxes):
    for b1, b2 in boxes:
        if min(p1[0], p2[0]) < b1 < max(p1[0], p2[0]) and min(p1[1], p2[1]) < b2 < max(
            p1[1], p2[1]
        ):
            return False
    return True


def outside_area(box, line):
    p1, p2 = line
    b1, b2 = box
    for dim in (0, 1):
        if max(p1[dim], p2[dim]) <= min(b1[dim], b2[dim]) or max(
            b1[dim], b2[dim]
        ) <= min(p1[dim], p2[dim]):
            return True
    return False


def all_outside(rect, lines):
    for line in lines:
        if not outside_area(rect, line):
            # print(f"line {line} inside rect {rect}")
            return False
    return True


if __name__ == "__main__":

    with open(0) as data:
        puzzle_input = data.read().splitlines()

    tiles = [tuple(map(int, x.split(","))) for x in puzzle_input]

    rectangles = [(x, y) for i, x in enumerate(tiles) for y in tiles[i + 1 :]]
    areas = list(map(area, rectangles))
    rectangles.sort(key=area, reverse=True)
    # print(area(rectangles[0]))
    # print(rectangles)

    lines = [(x, tiles[(i + 1) % len(tiles)]) for i, x in enumerate(tiles)]
    # print(lines)

    for rect in rectangles:
        if all_outside(rect, lines):
            p1, p2 = rect
            print(f"{p1} <--> {p2} area={area((p1,p2))}")
            break
