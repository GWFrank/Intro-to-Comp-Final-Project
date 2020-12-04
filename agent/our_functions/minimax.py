from eval_funcs import positionalEval
from make_move import makeMove
from available_spot import getAvailableSpot
evalBoard = positionalEval

def minimax(obs,color,depth):
    '''
    Find optimal position in the game.

    - inputs
      obs: 1d list, current board. white = 1, black = -1, empty = 0
      color: int, player color. same as obs
      depth: int, layers to search through.
      evalBoard: function that takes a board to evaluate, returns an integer. 
                 larger value if white is more likely to win, vise versa.

    - output
      tuple: best position
      integer: value
    '''
    
    if depth == 0:
        return None, evalBoard(obs)

    moves = getAvailableSpot(obs, color)
    if color == 1:
        value = -float('inf')
        bestmove = None
        if len(moves) == 0: # no move, proceed to other player
            _ ,newValue = minimax(obs, -color, depth-1)
            if newValue > value:
                value = newValue
            
        for move in moves:
            newBoard = makeMove(obs, move, color)
            _ ,newValue = minimax(newBoard, -color, depth-1)
            if newValue > value:
                value = newValue
                bestmove = move
    else:
        value = float('inf')
        bestmove = None
        if len(moves) == 0:
            _, newValue = minimax(obs, -color, depth-1)
            if newValue < value:
                value = newValue
        for move in moves:
            newBoard = makeMove(obs, move, color)
            _ ,newValue = minimax(newBoard, -color, depth-1)
            if newValue < value:
                value = newValue
                bestmove = move

    return bestmove, value
