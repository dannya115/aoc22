import re

# Parse input data 
with open("aoc5_input.txt") as fh:
    aoc_input = fh.read()

move_data = aoc_input.split("\n")[10:-1]
all_moves = []

delimiters = "move ", " from ", " to "
regex_pattern = "|".join(delimiters)

for move in move_data:
    all_moves.append([int(i) for i in re.split(regex_pattern, move)[1:]])

# Generate crates array
crates = [
    ['W', 'M', 'L', 'F'],
    ['B', 'Z', 'V', 'M', 'F'],
    ['H', 'V', 'R', 'S', 'L', 'Q'],
    ['F', 'S', 'V', 'Q', 'P', 'M', 'T', 'J'],
    ['L', 'S', 'W'],
    ['F', 'V', 'P', 'M', 'R', 'J', 'W'],
    ['J', 'Q', 'C', 'P', 'N', 'R', 'F'],
    ['V', 'H', 'P', 'S', 'Z', 'W', 'R', 'B'],
    ['B', 'M', 'J', 'C', 'G', 'H', 'Z', 'W']
]

# Iterate through all moves and update crates
for move in all_moves:
    crates[move[2]-1] += crates[move[1]-1][-move[0]:]
    crates[move[1]-1] = crates[move[1]-1][:-move[0]]


# Print final answer
answer = ""
for column in crates:
    answer += column[-1]

print(answer)