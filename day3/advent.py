import re

if __name__ == "__main__":

    with open(0) as data:
        puzzle_input = data.read()

    skip = re.compile(r"don\'t\(\).*?do\(\)")
    enabled = skip.sub('-', puzzle_input)

    p = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    instrs = p.findall(enabled)
    sum = 0
    for (x, y) in instrs:
        sum += int(x)*int(y)

    print(sum)

