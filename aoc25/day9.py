def area(points):
    point1, point2 = points

    return (abs(point2[0] - point1[0]) + 1) * (abs(point2[1] - point1[1]) + 1)


if __name__ == "__main__":

    with open(0) as data:
        puzzle_input = data.read().splitlines()

    boxes = [tuple(map(int, x.split(","))) for x in puzzle_input]

    pairs = [(x, y) for i, x in enumerate(boxes) for y in boxes[i + 1 :]]
    areas = list(map(area, pairs))
    areas.sort()

    print(areas[-1])
