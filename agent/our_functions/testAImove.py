from minimax import minimax
board = [0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 1, 1,
         0, 0, 0, 0, 0, 0, 1, -1,
         0, 0, 1, 1, 1, 1, 1, 0,
         0, 0, 1, 0, 1, -1, -1, 0]

move, value = minimax(board,1,5)
print(move)
print(value)