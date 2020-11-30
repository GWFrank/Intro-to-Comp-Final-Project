from evalBoard import evalBoard
def minimax(obs,color,depth):
    '''
    Find optimal position in the game.

    - inputs
      obs: 2d list, current board. white = 1, black = -1, empty = 0
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

    moves = getAvailableSpot(obs)
    if color == 1:
        value = -float('inf')
        bestmove = None
        for move in moves:
            newBoard = getBoardAfterMove(obs, move, color)
            _ ,newValue = minimax(newBoard, -color, depth-1)
            if newValue > value:
                value = newValue
                bestmove = move
    else:
        value = float('inf')
        bestmove = None
        for move in moves:
            _ ,newValue = minimax(newBoard, -color, depth-1)
            newValue = evalBoard(newBoard)
            if newValue < value:
                value = newValue
                bestmove = move

    return bestmove, value
