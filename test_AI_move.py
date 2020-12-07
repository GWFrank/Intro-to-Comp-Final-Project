import numpy as np
import time # timer

from agent.our_functions.minimax import minimax
from agent.our_functions.make_move import makeMove
from agent.our_functions.available_spot import getAvailableSpot

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


start = time.time() # timer
color = -1
nomovecount = 0
colorName = {1: 'white', -1: 'black'}
while nomovecount <= 2:
    move, value = minimax(board, color, 5, -float('inf'), float('inf'))
    
    try:
        print(f"{colorName[color]} move in {(move%8, move//8)} with value {value}") # print
        # print(f"available spots : {getAvailableSpot(board, color)}") # print
        board = makeMove(board, move, color)
        nomovecount = 0
        printBoard(board) # print
        print("="*20) # print
    except:
        nomovecount += 1
        pass
    
    color = -color

end = time.time() # timer
print(f"a game takes {end-start:.3f}s") # timer
print("board sum : ", sum(board))