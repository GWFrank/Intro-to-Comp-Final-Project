from minimax import minimax
from make_move import makeMove
import time # timer
# from available_spot
def printBoard(obs):
    for i in range(8):
        for j in range(8):
            if obs[i*8+j] == 0:
                print('_', end='')
            if obs[i*8+j] == 1:
                print('O', end='')
            if obs[i*8+j] == -1:
                print('X', end='')
        print('')

board = [0,  0,  0,  0,  0,  0,  0,  0,
         0,  0,  0,  0,  0,  0,  0,  0,
         0,  0,  0,  0,  0,  0,  0,  0,
         0,  0,  0,  1, -1,  0,  0,  0,
         0,  0,  0, -1,  1,  0,  0,  0,
         0,  0,  0,  0,  0,  0,  0,  0,
         0,  0,  0,  0,  0,  0,  0,  0,
         0,  0,  0,  0,  0,  0,  0,  0]

color = -1
nomovecount = 0
colorName = {1: 'white', -1: 'black'}
start = time.time() # timer
while nomovecount <=2:
    move, value = minimax(board, color, 4)
    print(move)
    print(value)
    if move:
        board = makeMove(board, move, color)
        nomovecount = 0
    else:
        nomovecount += 1
    printBoard(board)
    color = -color
    
end = time.time() # timer
print(f" {end-start:.3f}s") # timer

