with open("day_04/aoc4_input.txt") as fh:
    aoc_input = fh.read()

all_pairs = aoc_input.split("\n")[:-1]
split_pairs = []
counter = 0
overlap_counter = 0

for pair in all_pairs:
    split_pair = pair.split(",")
    nums_list = []
    for num in split_pair:
        nums_list.append([int(i) for i in num.split("-")])
    
    split_pairs.append(nums_list)

for pair in split_pairs:
    pair1 = pair[0]
    pair2 = pair[1]

    if (pair1[0] <= pair2[0] and pair1[1] >= pair2[1]) or (pair2[0] <= pair1[0] and pair2[1] >= pair1[1]):
        counter += 1
    
    if (pair1[1] >= pair2[0] and pair1[0] <= pair2[0]) or (pair2[1] >= pair1[0] and pair2[0] <= pair1[0]):
        overlap_counter += 1


print(overlap_counter)