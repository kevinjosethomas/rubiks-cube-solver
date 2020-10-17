import display

solved_cube = [
    [
        ["w","w","w"],
        ["w","W","w"],
        ["w","w","w"]
    ],
    [
        ["g","g","g"],
        ["g","G","g"],
        ["g","g","g"]
    ],
    [
        ["r","r","r"],
        ["r","R","r"],
        ["r","r","r"]
    ],
    [
        ["b","b","b"],
        ["b","B","b"],
        ["b","b","b"]
    ],
    [
        ["o","o","o"],
        ["o","O","o"],
        ["o","o","o"]
    ],
    [
        ["y","y","y"],
        ["y","Y","y"],
        ["y","y","y"]
    ]
]

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

display.display_cube(solved_cube)
