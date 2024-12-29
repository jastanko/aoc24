def is_calibrated(test, first, rest):
    if len(rest) = 0:
        return test == first
    else:
        first += rest[0]
        return is_calibrated(test, first, {})

if __name__ == "__main__":

    test = 190
    list = [10, 19]
    rest = list[1:]
    print(rest)
    print(is_calibrated(test, 10, rest))
