# Parse input data as list of moves
with open("day_09/aoc9_input.txt") as fh:
    aoc_input = fh.read()
    aoc_input = aoc_input.splitlines()

moves = [move.split() for move in aoc_input]

# Initialise dictionary for moves
moves_dict = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0)
}

differences = {
    (2, 0): (1, 0),
    (-2, 0): (-1, 0),
    (0, 2): (0, 1),
    (0, -2): (0, -1),
    (1, 2): (1, 1),
    (2, 1): (1, 1),
    (2, -1): (1, -1),
    (1, -2): (1, -1),
    (-1, -2): (-1, -1),
    (-2, -1): (-1, -1),
    (-2, 1): (-1, 1),
    (-1, 2): (-1, 1),
    ### Additional differences for part 2
    (2, 2): (1, 1),
    (2, -2): (1, -1),
    (-2, 2): (-1, 1),
    (-2, -2): (-1, -1)
}

# Helper functions
def add(current, move):
    return tuple(a+b for a, b in zip(current, move))

def subtract(head, tail):
    return tuple(a-b for a, b in zip(head, tail))

def are_touching(head, tail):
    return (head[0] - tail[0] >= -1 and head[0] - tail[0] <= 1) and (head[1] - tail[1] >= -1 and head[1] - tail[1] <= 1) 

def new_tail(new_head, current_tail):
    difference = subtract(new_head, current_tail)
    return add(current_tail, differences[difference])

# Part 1
def part_1():
    # Visited coordinates (initialised at starting coordinate)
    visited = {(0, 0): None}

    # Initialise H and T starting locations
    current_head = (0, 0)
    current_tail = (0, 0)

    for move in moves:
        direction, num_moves = move[0], int(move[1])
        for i in range(num_moves):
            new_head = add(current_head, moves_dict[direction])
            if are_touching(new_head, current_tail) is False:
                current_tail = new_tail(new_head, current_tail)
                if current_tail not in visited:
                    visited[current_tail] = None

            current_head = new_head
    
    return visited


# Part 2
def part_2():
    # Visited coordinates for tail (node 9)
    visited = {(0, 0): None}

    # Initialise starting locations
    all_nodes = [(0, 0) for i in range(10)]

    for move in moves:
        direction, num_moves = move[0], int(move[1])
        for i in range(num_moves):
            all_nodes[0] = add(all_nodes[0], moves_dict[direction])
            for node_idx in range(0, len(all_nodes)-1):
                if are_touching(all_nodes[node_idx], all_nodes[node_idx+1]) is False:
                    all_nodes[node_idx+1] = new_tail(all_nodes[node_idx], all_nodes[node_idx+1])
                    if all_nodes[-1] not in visited:
                        visited[all_nodes[-1]] = None
    
    return visited








