def is_calibrated(test, first, rest):
    if len(rest) == 0:
        return test == first
    elif first > test:
        return False
    else:
        return (
            is_calibrated(test, first + rest[0], rest[1:])
            or is_calibrated(test, first * rest[0], rest[1:])
            or is_calibrated(test, int("{}{}".format(first, rest[0])), rest[1:])
        )


if __name__ == "__main__":

    sum = 0
    for line in open(0).read().splitlines():
        equation = line.split(":")
        test = int(equation[0])
        rest = list(map(int, equation[1].split()))
        if is_calibrated(test, rest[0], rest[1:]):
            sum += test

    print(sum)
