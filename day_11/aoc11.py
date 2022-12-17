# Input data
all_items = [
    [77, 69, 76, 77, 50, 58],
    [75, 70, 82, 83, 96, 64, 62],
    [53],
    [85, 64, 93, 64, 99],
    [61, 92, 71],
    [79, 73, 50, 90],
    [50, 89],
    [83, 56, 64, 58, 93, 91, 56, 65]
]

# Helper functions
# operation - implements unique operation and then divides by 3
def operation(idx, item):
    if idx == 0:
        item = item * 11
    if idx == 1:
        item = item + 8
    if idx == 2:
        item = item * 3
    if idx == 3:
        item = item + 4
    if idx == 4:
        item = item ** 2
    if idx == 5:
        item = item + 2
    if idx == 6:
        item = item + 3
    if idx == 7:
        item = item + 5
    
    # return item // 3
    return item

# test - takes in monkey index and item after operations, returns monkey to go to
def test(idx, item):
    if idx == 0:
        if item % 5 == 0:
            return 1
        return 5
    if idx == 1:
        if item % 17 == 0:
            return 5
        return 6
    if idx == 2:
        if item % 2 == 0:
            return 0
        return 7
    if idx == 3:
        if item % 7 == 0:
            return 7
        return 2
    if idx == 4:
        if item % 3 == 0:
            return 2
        return 3
    if idx == 5:
        if item % 11 == 0:
            return 4
        return 6
    if idx == 6:
        if item % 13 == 0:
            return 4
        return 3
    if idx == 7:
        if item % 19 == 0:
            return 1
        return 0

# Part 1
def part_1():
    rounds = 20
    visits = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(rounds):
        for idx, monkey_items in enumerate(all_items):
            while len(monkey_items) > 0:
                current_item = monkey_items.pop(0)
                new_item = operation(idx, current_item)
                new_index = test(idx, new_item)
                all_items[new_index] += [new_item]
                
                visits[idx] = visits[idx] + 1

    sorted_visits = sorted(visits)

    return sorted_visits[-1] * sorted_visits[-2]

# Part 2
def part_2():
    rounds = 10000
    visits = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(1, rounds+1):
        for idx, monkey_items in enumerate(all_items):
            while len(monkey_items) > 0:
                current_item = monkey_items.pop(0)
                new_item = operation(idx, current_item)

                

                new_index = test(idx, new_item)
                all_items[new_index] += [new_item]
                
                visits[idx] = visits[idx] + 1

    sorted_visits = sorted(visits)

    return sorted_visits[-1] * sorted_visits[-2]

print(part_2())
