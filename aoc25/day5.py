def overlaps(r1, r2):
    return not (r1[1] < r2[0] or r1[0] > r2[1])


def union(fresh_ids, fmin, fmax):
    for i, frange in enumerate(fresh_ids):
        if overlaps(frange, (fmin, fmax)):
            fresh_ids.pop(i)
            return union(fresh_ids, min(frange[0], fmin), max(frange[1], fmax))

    fresh_ids.append([fmin, fmax])


if __name__ == "__main__":

    with open(0) as data:
        puzzle_input = data.read()

    in_ranges = True
    fresh_ids = []
    total = 0
    for line in puzzle_input.splitlines():
        if in_ranges:
            fresh_range = line.split("-")
            if len(fresh_range) < 2:
                in_ranges = False
            else:
                fmin = int(fresh_range[0])
                fmax = int(fresh_range[1])
                union(fresh_ids, fmin, fmax)
        else:
            for fresh_min, fresh_max in fresh_ids:
                if int(line) >= fresh_min and int(line) <= fresh_max:
                    total += 1
                    break

    print(fresh_ids)
    all_fresh = 0
    for fmin, fmax in fresh_ids:
        all_fresh += fmax - fmin + 1

    print(total)
    print(all_fresh)
