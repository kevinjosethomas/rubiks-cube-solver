import copy

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
    ]
]
"""

def u(cube):
    temp_cube = copy.deepcopy(cube)
    temp_cube[1][0] = cube[2][0]
    temp_cube[2][0] = cube[3][0]
    temp_cube[3][0] = cube[4][0]
    temp_cube[4][0] = cube[1][0]

    return temp_cube

def u_(cube):
    temp_cube = copy.deepcopy(cube)
    temp_cube[2][0] = cube[1][0]
    temp_cube[3][0] = cube[2][0]
    temp_cube[4][0] = cube[3][0]
    temp_cube[1][0] = cube[4][0]

    return temp_cube

def d(cube):
    temp_cube = copy.deepcopy(cube)
    temp_cube[1][2] = cube[2][2]
    temp_cube[2][2] = cube[3][2]
    temp_cube[3][2] = cube[4][2]
    temp_cube[4][2] = cube[1][2]

    return temp_cube

def d_(cube):
    temp_cube = copy.deepcopy(cube)
    temp_cube[2][2] = cube[1][2]
    temp_cube[3][2] = cube[2][2]
    temp_cube[4][2] = cube[3][2]
    temp_cube[1][2] = cube[4][2]

    return temp_cube

def f(cube):
    temp_cube = copy.deepcopy(cube)

    # Top Edge
    temp_cube[2][0][2] = cube[2][0][0]
    temp_cube[2][1][2] = cube[2][0][1]
    temp_cube[2][2][2] = cube[2][0][2]

    # Right Edge
    temp_cube[2][2][1] = cube[2][1][2]
    temp_cube[2][2][0] = cube[2][2][2]

    # Bottom Edge
    temp_cube[2][1][0] = cube[2][2][1]
    temp_cube[2][0][0] = cube[2][2][0]

    # Left Edge
    temp_cube[2][0][1] = cube[2][1][0]


    # Right -> Top
    temp_cube[3][0][0] = cube[0][2][0]
    temp_cube[3][1][0] = cube[0][2][1]
    temp_cube[3][2][0] = cube[0][2][2]

    # Bottom -> Right
    temp_cube[5][0][2] = cube[3][0][0]
    temp_cube[5][0][1] = cube[3][1][0]
    temp_cube[5][0][0] = cube[3][2][0]

    # Left -> Bottom
    temp_cube[1][0][2] = cube[5][0][0]
    temp_cube[1][1][2] = cube[5][0][1]
    temp_cube[1][2][2] = cube[5][0][2]

    # Top -> Left
    temp_cube[0][2][2] = cube[1][0][2]
    temp_cube[0][2][1] = cube[1][1][2]
    temp_cube[0][2][0] = cube[1][2][2]

    return temp_cube

def f_(cube):
    temp_cube = copy.deepcopy(cube)

    # Top Edge
    temp_cube[2][0][0] = cube[2][0][2]
    temp_cube[2][0][1] = cube[2][1][2]
    temp_cube[2][0][2] = cube[2][2][2]

    # Right Edge
    temp_cube[2][1][2] = cube[2][2][1]
    temp_cube[2][2][2] = cube[2][2][0]

    # Bottom Edge
    temp_cube[2][2][1] = cube[2][1][0]
    temp_cube[2][2][0] = cube[2][0][0]

    # Left Edge
    temp_cube[2][1][0] = cube[2][0][1]


    # Right -> Top
    temp_cube[0][2][0] = cube[3][0][0]
    temp_cube[0][2][1] = cube[3][1][0]
    temp_cube[0][2][2] = cube[3][2][0]

    # Bottom -> Right
    temp_cube[3][0][0] = cube[5][0][2]
    temp_cube[3][1][0] = cube[5][0][1]
    temp_cube[3][2][0] = cube[5][0][0]

    # Left -> Bottom
    temp_cube[5][0][0] = cube[1][0][2]
    temp_cube[5][0][1] = cube[1][1][2]
    temp_cube[5][0][2] = cube[1][2][2]

    # Top -> Left
    temp_cube[1][0][2] = cube[0][2][2]
    temp_cube[1][1][2] = cube[0][2][1]
    temp_cube[1][2][2] = cube[0][2][0]

    return temp_cube



"""
white - 0
green - 1
red - 2
blue - 3
orange - 4
yellow = 5
"""
