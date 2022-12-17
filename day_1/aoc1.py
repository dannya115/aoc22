with open('aoc1_input.txt') as fh:
    aoc_input = fh.read()

elf_calories = aoc_input.split("\n\n")

sum_calories = [cals.split("\n") if "\n" in cals else cals for cals in elf_calories]

current_top = []

for elf in sum_calories[:-1]:
    total = 0
    if type(elf) == list:    
        for item in elf:
            total += int(item)
    elif type(elf) == str:
        total += int(elf)
    
    current_top.append(total)

print(sorted(current_top))
print(sum(sorted(current_top)[-3:]))
print(66862 + 68330 + 70613)
