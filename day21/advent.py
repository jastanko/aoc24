KEYMAP = { "^" : "<A",
           ">" : "vA",
           "v" : "v<A",
           "<" : "v<<A"}
BACKMAP = { "^" : ">A",
           ">" : "^A",
           "v" : "^>A",
           "<" : ">>^A"}

def encode(keys):
    seq = ""
    prev = ""
    for i, key in enumerate(keys):
        if key == "A":
            seq += BACKMAP[prev]
        elif key == prev:
            seq += "A"
        else:
            seq += KEYMAP[key]
        prev = key
    return seq


if __name__ == "__main__":

    with open(0) as data:
        puzzle_input = data.read().splitlines()

    line = puzzle_input[0]
    print(encode(line))

