import copy

# Clockwise Rotations

def u(cube: list):
    temp_cube = copy.deepcopy(cube)

    # Changing same color
    temp_cube[1][0] = cube[2][0]
    temp_cube[2][0] = cube[3][0]
    temp_cube[3][0] = cube[4][0]
    temp_cube[4][0] = cube[1][0]

    # Changing around
    temp_cube[0][2][0] = cube[0][2][2]
    temp_cube[0][2][1] = cube[0][1][2]
    temp_cube[0][2][2] = cube[0][0][2]

    temp_cube[0][1][2] = cube[0][0][1]
    temp_cube[0][0][2] = cube[0][0][0]

    temp_cube[0][0][1] = cube[0][1][0]
    temp_cube[0][2][0] = cube[0][2][2]

    temp_cube[0][0][0] = cube[0][2][0]
    temp_cube[0][1][0] = cube[0][2][1]

    return temp_cube

def l(cube: list):
    temp_cube = copy.deepcopy(cube)

    # Changing same color
    temp_cube[1][0][0] = cube[1][2][0]
    temp_cube[1][0][1] = cube[1][1][0]
    temp_cube[1][0][2] = cube[1][0][0]

    temp_cube[1][1][2] = cube[1][0][1]
    temp_cube[1][2][2] = cube[1][0][2]

    temp_cube[1][2][1] = cube[1][1][2]
    temp_cube[1][2][0] = cube[1][2][2]

    temp_cube[1][1][0] = cube[1][2][1]

    # Changing around
    temp_cube[5][0][0] = cube[2][0][0]
    temp_cube[5][1][0] = cube[2][1][0]
    temp_cube[5][2][0] = cube[2][2][0]

    temp_cube[4][2][2] = cube[5][0][0]
    temp_cube[4][1][2] = cube[5][1][0]
    temp_cube[4][0][2] = cube[5][2][0]

    temp_cube[0][0][0] = cube[4][2][2]
    temp_cube[0][1][0] = cube[4][1][2]
    temp_cube[0][2][0] = cube[4][0][2]

    temp_cube[2][0][0] = cube[0][0][0]
    temp_cube[2][1][0] = cube[0][1][0]
    temp_cube[2][2][0] = cube[0][2][0]

    return temp_cube

def f(cube: list):
    temp_cube = copy.deepcopy(cube)

    # Changing same color
    temp_cube[2][0][2] = cube[2][0][0]
    temp_cube[2][1][2] = cube[2][0][1]
    temp_cube[2][2][2] = cube[2][0][2]

    temp_cube[2][2][1] = cube[2][1][2]
    temp_cube[2][2][0] = cube[2][2][2]

    temp_cube[2][1][0] = cube[2][2][1]
    temp_cube[2][0][0] = cube[2][2][0]

    temp_cube[2][0][1] = cube[2][1][0]


    # Changing around
    temp_cube[3][0][0] = cube[0][2][0]
    temp_cube[3][1][0] = cube[0][2][1]
    temp_cube[3][2][0] = cube[0][2][2]

    temp_cube[5][0][2] = cube[3][0][0]
    temp_cube[5][0][1] = cube[3][1][0]
    temp_cube[5][0][0] = cube[3][2][0]

    temp_cube[1][0][2] = cube[5][0][0]
    temp_cube[1][1][2] = cube[5][0][1]
    temp_cube[1][2][2] = cube[5][0][2]

    temp_cube[0][2][2] = cube[1][0][2]
    temp_cube[0][2][1] = cube[1][1][2]
    temp_cube[0][2][0] = cube[1][2][2]

    return temp_cube

def r(cube: list):
    temp_cube = copy.deepcopy(cube)

    # Changing same color
    temp_cube[3][0][0] = cube[3][2][0]
    temp_cube[3][0][1] = cube[3][1][0]
    temp_cube[3][0][2] = cube[3][0][0]

    temp_cube[3][1][2] = cube[3][0][1]
    temp_cube[3][2][2] = cube[3][0][2]

    temp_cube[3][2][1] = cube[3][1][2]
    temp_cube[3][2][0] = cube[3][2][2]

    temp_cube[3][1][0] = cube[3][2][1]

    # Changing around
    temp_cube[2][0][2] = cube[5][0][2]
    temp_cube[2][1][2] = cube[5][1][2]
    temp_cube[2][2][2] = cube[5][2][2]

    temp_cube[5][0][2] = cube[4][2][0]
    temp_cube[5][1][2] = cube[4][1][0]
    temp_cube[5][2][2] = cube[4][0][0]

    temp_cube[4][2][0] = cube[0][0][2]
    temp_cube[4][1][0] = cube[0][1][2]
    temp_cube[4][0][0] = cube[0][2][2]

    temp_cube[0][0][2] = cube[2][0][2]
    temp_cube[0][1][2] = cube[2][1][2]
    temp_cube[0][2][2] = cube[2][2][2]

    return temp_cube

def b(cube: list):
    temp_cube = copy.deepcopy(cube)

    # Changing same color
    temp_cube[4][0][2] = cube[4][0][0]
    temp_cube[4][1][2] = cube[4][0][1]
    temp_cube[4][2][2] = cube[4][0][2]

    temp_cube[4][2][1] = cube[4][1][2]
    temp_cube[4][2][0] = cube[4][2][2]

    temp_cube[4][1][0] = cube[4][2][1]
    temp_cube[4][0][0] = cube[4][2][0]

    temp_cube[4][0][1] = cube[4][1][0]

    # Changing around
    temp_cube[0][0][0] = cube[3][0][2]
    temp_cube[0][0][1] = cube[3][1][2]
    temp_cube[0][0][2] = cube[3][2][2]

    temp_cube[3][0][2] = cube[5][2][2]
    temp_cube[3][1][2] = cube[5][2][1]
    temp_cube[3][2][2] = cube[5][2][0]

    temp_cube[5][2][0] = cube[1][0][0]
    temp_cube[5][2][1] = cube[1][1][0]
    temp_cube[5][2][2] = cube[1][2][0]

    temp_cube[1][0][0] = cube[0][0][2]
    temp_cube[1][1][0] = cube[0][0][1]
    temp_cube[1][2][0] = cube[0][0][0]

    return temp_cube

def d(cube: list):
    temp_cube = copy.deepcopy(cube)

    # Changing same color
    temp_cube[2][2] = cube[1][2]
    temp_cube[3][2] = cube[2][2]
    temp_cube[4][2] = cube[3][2]
    temp_cube[1][2] = cube[4][2]

    # Changing around
    temp_cube[5][2][0] = cube[5][2][2]
    temp_cube[5][2][1] = cube[5][1][2]
    temp_cube[5][2][2] = cube[5][0][2]

    temp_cube[5][1][2] = cube[5][0][1]
    temp_cube[5][0][2] = cube[5][0][0]

    temp_cube[5][0][1] = cube[5][1][0]
    temp_cube[5][2][0] = cube[5][2][2]

    temp_cube[5][0][0] = cube[5][2][0]
    temp_cube[5][1][0] = cube[5][2][1]

    return temp_cube


# Counterclockwise Rotations

def u_(cube: list):
    temp_cube = copy.deepcopy(cube)

    # Changing same color
    temp_cube[2][0] = cube[1][0]
    temp_cube[3][0] = cube[2][0]
    temp_cube[4][0] = cube[3][0]
    temp_cube[1][0] = cube[4][0]

    # Changing around
    temp_cube[0][2][2] = cube[0][2][0]
    temp_cube[0][1][2] = cube[0][2][1]
    temp_cube[0][0][2] = cube[0][2][2]

    temp_cube[0][0][1] = cube[0][1][2]
    temp_cube[0][0][0] = cube[0][0][2]

    temp_cube[0][1][0] = cube[0][0][1]
    temp_cube[0][2][2] = cube[0][2][0]

    temp_cube[0][2][0] = cube[0][0][0]
    temp_cube[0][2][1] = cube[0][1][0]

    return temp_cube

def l_(cube: list):
    temp_cube = copy.deepcopy(cube)

    # Changing same color
    temp_cube[1][2][0] = cube[1][0][0]
    temp_cube[1][1][0] = cube[1][0][1]
    temp_cube[1][0][0] = cube[1][0][2]

    temp_cube[1][0][1] = cube[1][1][2]
    temp_cube[1][0][2] = cube[1][2][2]

    temp_cube[1][1][2] = cube[1][2][1]
    temp_cube[1][2][2] = cube[1][2][0]

    temp_cube[1][2][1] = cube[1][1][0]

    # Changing around
    temp_cube[2][0][0] = cube[5][0][0]
    temp_cube[2][1][0] = cube[5][1][0]
    temp_cube[2][2][0] = cube[5][2][0]

    temp_cube[5][0][0] = cube[4][2][2]
    temp_cube[5][1][0] = cube[4][1][2]
    temp_cube[5][2][0] = cube[4][0][2]

    temp_cube[4][2][2] = cube[0][0][0]
    temp_cube[4][1][2] = cube[0][1][0]
    temp_cube[4][0][2] = cube[0][2][0]

    temp_cube[0][0][0] = cube[2][0][0]
    temp_cube[0][1][0] = cube[2][1][0]
    temp_cube[0][2][0] = cube[2][2][0]

    return temp_cube

def f_(cube: list):
    temp_cube = copy.deepcopy(cube)

    # Changing same color
    temp_cube[2][0][0] = cube[2][0][2]
    temp_cube[2][0][1] = cube[2][1][2]
    temp_cube[2][0][2] = cube[2][2][2]

    temp_cube[2][1][2] = cube[2][2][1]
    temp_cube[2][2][2] = cube[2][2][0]

    temp_cube[2][2][1] = cube[2][1][0]
    temp_cube[2][2][0] = cube[2][0][0]

    temp_cube[2][1][0] = cube[2][0][1]

    # Changing around
    temp_cube[0][2][0] = cube[3][0][0]
    temp_cube[0][2][1] = cube[3][1][0]
    temp_cube[0][2][2] = cube[3][2][0]

    temp_cube[3][0][0] = cube[5][0][2]
    temp_cube[3][1][0] = cube[5][0][1]
    temp_cube[3][2][0] = cube[5][0][0]

    temp_cube[5][0][0] = cube[1][0][2]
    temp_cube[5][0][1] = cube[1][1][2]
    temp_cube[5][0][2] = cube[1][2][2]

    temp_cube[1][0][2] = cube[0][2][2]
    temp_cube[1][1][2] = cube[0][2][1]
    temp_cube[1][2][2] = cube[0][2][0]

    return temp_cube

def r_(cube: list):
    temp_cube = copy.deepcopy(cube)

    # Changing same color
    temp_cube[3][2][0] = cube[3][0][0]
    temp_cube[3][1][0] = cube[3][0][1]
    temp_cube[3][0][0] = cube[3][0][2]

    temp_cube[3][0][1] = cube[3][1][2]
    temp_cube[3][0][2] = cube[3][2][2]

    temp_cube[3][1][2] = cube[3][2][1]
    temp_cube[3][2][2] = cube[3][2][0]

    temp_cube[3][2][1] = cube[3][1][0]

    # Changing around
    temp_cube[5][0][2] = cube[2][0][2]
    temp_cube[5][1][2] = cube[2][1][2]
    temp_cube[5][2][2] = cube[2][2][2]

    temp_cube[4][2][0] = cube[5][0][2]
    temp_cube[4][1][0] = cube[5][1][2]
    temp_cube[4][0][0] = cube[5][2][2]

    temp_cube[0][0][2] = cube[4][2][0]
    temp_cube[0][1][2] = cube[4][1][0]
    temp_cube[0][2][2] = cube[4][0][0]

    temp_cube[2][0][2] = cube[0][0][2]
    temp_cube[2][1][2] = cube[0][1][2]
    temp_cube[2][2][2] = cube[0][2][2]

    return temp_cube

def b_(cube: list):
    temp_cube = copy.deepcopy(cube)

    # Changing same color
    temp_cube[4][0][0] = cube[4][0][2]
    temp_cube[4][0][1] = cube[4][1][2]
    temp_cube[4][0][2] = cube[4][2][2]

    temp_cube[4][1][2] = cube[4][2][1]
    temp_cube[4][2][2] = cube[4][2][0]

    temp_cube[4][2][1] = cube[4][1][0]
    temp_cube[4][2][0] = cube[4][0][0]

    temp_cube[4][1][0] = cube[4][0][1]


    # Changing around
    temp_cube[3][0][2] = cube[0][0][0]
    temp_cube[3][1][2] = cube[0][0][1]
    temp_cube[3][2][2] = cube[0][0][2]

    temp_cube[5][2][2] = cube[3][0][2]
    temp_cube[5][2][1] = cube[3][1][2]
    temp_cube[5][2][0] = cube[3][2][2]

    temp_cube[1][0][0] = cube[5][2][0]
    temp_cube[1][1][0] = cube[5][2][1]
    temp_cube[1][2][0] = cube[5][2][2]

    temp_cube[0][0][2] = cube[1][0][0]
    temp_cube[0][0][1] = cube[1][1][0]
    temp_cube[0][0][0] = cube[1][2][0]

    return temp_cube

def d_(cube: list):
    temp_cube = copy.deepcopy(cube)

    # Changing same color
    temp_cube[1][2] = cube[2][2]
    temp_cube[2][2] = cube[3][2]
    temp_cube[3][2] = cube[4][2]
    temp_cube[4][2] = cube[1][2]

    # Changing around
    temp_cube[5][2][2] = cube[5][2][0]
    temp_cube[5][1][2] = cube[5][2][1]
    temp_cube[5][0][2] = cube[5][2][2]

    temp_cube[5][0][1] = cube[5][1][2]
    temp_cube[5][0][0] = cube[5][0][2]

    temp_cube[5][1][0] = cube[5][0][1]
    temp_cube[5][2][2] = cube[5][2][0]

    temp_cube[5][2][0] = cube[5][0][0]
    temp_cube[5][2][1] = cube[5][1][0]

    return temp_cube


# Slice Turns

def m(cube: list):
    temp_cube = copy.deepcopy(cube)

    temp_cube = r(temp_cube)
    temp_cube = l_(temp_cube)

    return temp_cube

def m_(cube: list):
    temp_cube = copy.deepcopy(cube)

    temp_cube = r_(temp_cube)
    temp_cube = l(temp_cube)

    return temp_cube

def e(cube: list):
    temp_cube = copy.deepcopy(cube)

    temp_cube = u(temp_cube)
    temp_cube = d_(temp_cube)

    return temp_cube

def e_(cube: list):
    temp_cube = copy.deepcopy(cube)

    temp_cube = u_(temp_cube)
    temp_cube = d(temp_cube)

    return temp_cube

def s(cube: list):
    temp_cube = copy.deepcopy(cube)

    temp_cube = f_(temp_cube)
    temp_cube = b(temp_cube)

    return temp_cube

def s_(cube: list):
    temp_cube = copy.deepcopy(cube)

    temp_cube = f(temp_cube)
    temp_cube = b_(temp_cube)

    return temp_cube
