import numpy as np

# Parse data into numpy array
with open("aoc8_input.txt") as fh:
    aoc_input = fh.read()

input = aoc_input.split("\n")[:-1]
trees_array = []

for row in input:
    trees_array.append([int(i) for i in row])

trees_array = np.array(trees_array)

# Get dimensions
num_rows, num_cols = trees_array.shape

# Initialise counter
total_visible = 2 * num_cols + 2 * num_rows - 4
current_max = 0

for row in range(1, num_rows-1):
    for col in range(1, num_cols-1):
        val = trees_array[row, col]
        num_up, num_down, num_left, num_right = 1, 1, 1, 1

        # Checking trees above
        for i, tree in enumerate(trees_array[:row, col][::-1]):
            if val > tree and i != len(trees_array[:row, col]) - 1:
                num_up += 1
            else:
                break

        # Checking trees below
        for i, tree in enumerate(trees_array[row+1:, col]):
            if val > tree and i != len(trees_array[row+1:, col]) - 1:
                num_down += 1
            else:
                break

        # Checking trees left
        for i, tree in enumerate(trees_array[row,:col][::-1]):
            if val > tree and i != len(trees_array[row,:col][::-1]) - 1:
                num_left += 1
            else:
                break
            
        # Checking trees right
        for i, tree in enumerate(trees_array[row, col+1:]):
            if val > tree and i != len(trees_array[row, col+1:]) - 1:
                num_right += 1
            else:
                break
            
        if num_up * num_down * num_left * num_right > current_max:
            current_max = num_up * num_down * num_left * num_right
            print(f"""Coords: ({row}, {col}). Value: {val}. ({num_up}, {num_down}, {num_left}, {num_right}). Current max: {current_max}.""")

        # if val > max(trees_array[:row, col]) or val > max(trees_array[row+1:, col]):
        #     total_visible += 1
        # elif val > max(trees_array[row, :col]) or val > max(trees_array[row, col+1:]):
        #     total_visible += 1

