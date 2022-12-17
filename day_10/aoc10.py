# Parse input data as list of moves - (0, 0) for 'noop' and (1, X) for 'addx X'
with open("aoc10_input.txt") as fh:
    aoc_input = fh.read()
    aoc_input = aoc_input.splitlines()

moves = [(0, 0) if move == 'noop' else (1, int(move.split()[-1])) for move in aoc_input]

def part_1():
    current_register = 1
    cycle_number = 1
    total_signal = 0
    cycles = [20, 60, 100, 140, 180, 220]

    for move in moves:
        for i in range(move[0]+ 1):
            cycle_number += 1
            if cycle_number in cycles:
                total_signal += cycle_number * current_register
        
        current_register += move[1]
        print((cycle_number, current_register))

    return total_signal

def part_2():
    CRT_row = ""
    current_left_register = 1
    cycle_number = 0
    cycles = [40, 80, 120, 160, 200, 240]

    for move in moves:
        for i in range(move[0]+1):
            cycle_number += 1
            if cycle_number >= current_left_register and cycle_number <= current_left_register + 2:
                CRT_row += "#"
            else:
                CRT_row += "."
            
            if cycle_number in cycles:
                CRT_row += "\n"
                cycle_number = 0

        current_left_register += move[1]
    
    return CRT_row


