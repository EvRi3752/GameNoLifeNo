
def dead_state():
    board_state = [
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [1,0,1,1,1,1,1],
    [1,1,1,1,1,1,1]
]
    initialize = 0
    for i in board_state:
        initialize = initialize + i
        print(board_state)