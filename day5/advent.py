import re

if __name__ == "__main__":

    with open(0) as data:
        puzzle_input = data.read().splitlines()

    rules = []
    updates = []

    for line in puzzle_input:
        rule = line.split('|')
        if len(rule) == 2:
            rules.append(rule)
        update = line.split(',')
        if len(update) > 1:
            updates.append(rule)

    for update in updates:
        for rule in rules:
            loc_x = update.index(rule[0])
            loc_y = update.index(rule[1])
            if loc_x > loc_y > 1:
                print("update is invalid" + update)
                break
