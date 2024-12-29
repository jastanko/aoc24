def checksum(blocks):
    cs = 0
    for i in range(0, len(blocks)):
        if blocks[i] != ".":
            cs += int(blocks[i]) * i
    return cs

def map_blocks(diskmap):
    mapb = ""
    for i in range(0, len(diskmap)):
        ch = i%2 == 0 ? diskmap[i] : "."
        mapb += ch*i
    return mapb

if __name__ == "__main__":

    diskmap = open(0).read()
    blocks = map_blocks(diskmap)
    print(blocks)
    sum = checksum("0099811188827773336446555566..............")
    print(sum)
