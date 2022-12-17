with open("day_06/aoc6_input.txt") as fh:
    aoc_input = fh.read()

for i, letter in enumerate(aoc_input):
    if len(set(aoc_input[i:i+14])) == 14:
        print(i+14)
        break

