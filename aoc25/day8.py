from math import hypot

NUM_CONNECTIONS = 1000


def strline_distance(points):
    point1, point2 = points

    # Calculate the Euclidean distance between them
    return hypot(point2[0] - point1[0], point2[1] - point1[1], point2[2] - point1[2])


circuits = list()


def find_circuit(point):
    for circuit in circuits:
        if point in circuit:
            return circuit
    return None


if __name__ == "__main__":

    with open(0) as data:
        puzzle_input = data.read().splitlines()

    boxes = [tuple(map(int, x.split(","))) for x in puzzle_input]

    pairs = [(x, y) for i, x in enumerate(boxes) for y in boxes[i + 1 :]]
    pairs.sort(key=strline_distance)

    for p1, p2 in pairs[:NUM_CONNECTIONS]:
        c1 = find_circuit(p1)
        c2 = find_circuit(p2)
        # print(f"--- {p1}:{c1} <--> {p2}:{c2}")
        if c1 == None:
            if c2 == None:
                circuits.append({p1, p2})
            else:
                c2.add(p1)
        elif c2 == None:
            c1.add(p2)
        elif c1 != c2:
            circuits.remove(c1)
            circuits.remove(c2)
            circuits.append(c1.union(c2))
    clist = sorted(map(len, circuits))
    print(clist[-1] * clist[-2] * clist[-3])
