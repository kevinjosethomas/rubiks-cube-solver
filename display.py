from pprint import pprint

"""
[
    [
        ['g', 'g', 'g'],
        ['g', 'G', 'g'],
        ['g', 'g', 'g']
    ],
    [
        ['r', 'r', 'r'],
        ['r', 'R', 'r'],
        ['r', 'r', 'r']
    ],
    [
        ['b', 'b', 'b'],
        ['b', 'B', 'b'],
        ['b', 'b', 'b']
    ],
    [
        ['o', 'o', 'o'],
        ['o', 'O', 'o'],
        ['o', 'o', 'o']
    ]
]
"""

def display_cube(cube):

    middle = [cube[1], cube[2], cube[3], cube[4]]

    for side in cube[0]:
        print(" " * 7, end ="")
        print(" ".join(side), end="\n")

    for face in middle:
        newline = "\n" if middle.index(face) == len(middle) - 1 else "  "
        print(" ".join(face[0]) + newline, end="")
    for face in middle:
        newline = "\n" if middle.index(face) == len(middle) - 1 else "  "
        print(" ".join(face[1]) + newline, end="")
    for face in middle:
        newline = "\n" if middle.index(face) == len(middle) - 1 else "  "
        print(" ".join(face[2]) + newline, end="")
    for side in cube[5]:
        print(" " * 7, end="")
        print(" ".join(side))
