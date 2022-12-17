with open("aoc2_input.txt") as fh:
    aoc_input = fh.read()

all_plays = aoc_input.split("\n")[:-1]

rock_points = 1
paper_points = 2
scissors_points = 3
draw_points = 3
win_points = 6


play_dict = {

    "A X": scissors_points,
    "A Y": rock_points + draw_points,
    "A Z": paper_points + win_points,
    "B X": rock_points,
    "B Y": paper_points + draw_points,
    "B Z": scissors_points + win_points,
    "C X": paper_points,
    "C Y": scissors_points + draw_points,
    "C Z": rock_points + win_points

}

tot_score = 0

for play in all_plays:
    tot_score += play_dict[play]

print(tot_score)



# A, X --> rock (1)
# B, Y --> paper (2)
# C, Z --> scissors (3)