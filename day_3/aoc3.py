characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

priorities = {letter: i+1 for i, letter in zip(range(len(characters)), characters)}

with open("aoc3_input.txt") as fh:
    aoc_input = fh.read()

all_rucksacks = aoc_input.split("\n")[:-1]

total = 0

for i in range(0, len(all_rucksacks), 3):
    first_rucksack = set(all_rucksacks[i])
    second_rucksack = set(all_rucksacks[i+1])
    third_rucksack = set(all_rucksacks[i+2])
    badge = first_rucksack.intersection(second_rucksack, third_rucksack)
    total += priorities[badge.pop()]


# for rucksack in all_rucksacks:
#     first_rucksack = set(rucksack[:(len(rucksack)//2)])
#     second_rucksack = set(rucksack[(len(rucksack)//2):])
#     item_in_both = first_rucksack.intersection(second_rucksack)
#     total += priorities[item_in_both.pop()]

print(total)