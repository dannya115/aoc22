import numpy as np

# Parse input data as an array of heights ('a' --> 0, 'z' --> 25)
with open("day_12/aoc12_input.txt") as fh:
    aoc_input = fh.read()
    aoc_input = aoc_input.splitlines()

# Initially set 'S' --> 26, 'E' --> 27
letters = "abcdefghijklmnopqrstuvwxyzSE"
path_conversion = {letter: i for letter, i in zip(letters, range(len(letters)))}
hill_array = [[path_conversion[letter] for letter in row] for row in aoc_input]

# Turn array into numpy array
hill_array = np.array(hill_array)

# Get index of start and end nodes
start_coords = np.where(hill_array == 26)
start_coords = (start_coords[0][0], start_coords[1][0])
end_coords = np.where(hill_array == 27)
end_coords = (end_coords[0][0], end_coords[1][0])

# Replace start and end nodes with appropriate heights
hill_array[start_coords[0]][start_coords[1]] = 0
hill_array[end_coords[0]][end_coords[1]] = 25

# Define allowed moves (up, down, left, right)
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Helper functions
def add(start, move):
    return (start[0] + move[0], start[1] + move[1])

def valid_move(start, end):
    return hill_array[end[0]][end[1]] - hill_array[start[0]][start[1]] <= 1

def is_in_bounds(coords):
    x_hill, y_hill = add(hill_array.shape, (-1, -1))
    x_coord, y_coord = coords

    return (x_coord >= 0 and x_coord <= x_hill) and (y_coord >= 0 and y_coord <= y_hill)

def get_zero_coords():
    np_coords = np.where(hill_array == 0)
    return [((a, b), 0) for a, b in zip(np_coords[0], np_coords[1])]


# Part 1 - implementing BFS from start node until end node is reached
def part_1():
    visited = {}
    queue = [(start_coords, 0)]

    while len(queue) > 0:
        current_node = queue.pop(0)
        coords, step = current_node

        if coords == end_coords:
            return step

        if coords not in visited:
            visited[coords] = step

            for move in moves:
                new_node = add(coords, move)
                if is_in_bounds(new_node):
                    if valid_move(coords, new_node):
                        queue.append((add(coords, move), step+1))


# Part 2
def part_2():
    shortest_paths = []
    start_nodes = get_zero_coords()

    for start_coord in start_nodes:
        visited = {}
        queue = [start_coord]

        while len(queue) > 0:
            current_node = queue.pop(0)
            coords, step = current_node

            if coords == end_coords:
                shortest_paths.append(step)

            if coords not in visited:
                visited[coords] = step

                for move in moves:
                    new_node = add(coords, move)
                    if is_in_bounds(new_node):
                        if valid_move(coords, new_node):
                            queue.append((add(coords, move), step+1))
    
    return min(shortest_paths)


        

