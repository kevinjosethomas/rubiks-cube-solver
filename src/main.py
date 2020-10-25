import os
import time
import copy
import directions
from utility import *

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

# Prints solved cube
show(solved_cube)
