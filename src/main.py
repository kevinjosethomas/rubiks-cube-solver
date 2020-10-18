import os
import time
import copy
import display
import directions

solved_cube = [
    [
        ["w","w","w"],
        ["w","w","w"],
        ["w","w","w"]
    ],
    [
        ["g","g","g"],
        ["g","g","g"],
        ["g","g","g"]
    ],
    [
        ["r","r","r"],
        ["r","r","r"],
        ["r","r","r"]
    ],
    [
        ["b","b","b"],
        ["b","b","b"],
        ["b","b","b"]
    ],
    [
        ["o","o","o"],
        ["o","o","o"],
        ["o","o","o"]
    ],
    [
        ["y","y","y"],
        ["y","y","y"],
        ["y","y","y"]
    ]
]
cube = copy.deepcopy(solved_cube)

"""

       w w w
       w W w
       w w w
g g g  r r r  b b b  o o o
g G g  r R r  b B b  o O o
g g g  r r r  b b b  o o o
       y y y
       y Y y
       y y y

"""

# Prints solved cube
display.display_cube(solved_cube)

print("\n\n")
cube = directions.f(cube)
display.display_cube(cube)
print("\n\n")
time.sleep(1)

cube = directions.f_(cube)
display.display_cube(cube)
print("\n")
time.sleep(1)
