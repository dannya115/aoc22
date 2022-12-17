with open("day_07/aoc7_input.txt") as fh:
    aoc_input = fh.read()

input = aoc_input.split("\n")[:-1]

class Directory:

    def __init__(self, name: str, file_sum: int = 0, children: dict = {}, parent=None):
        self.name = name
        self.file_sum = file_sum
        self.children = children
        self.parent = parent
    

def create_tree():
    pass
