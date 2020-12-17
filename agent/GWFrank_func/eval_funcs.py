from random import random
def posEvalEndgameVariation(obs, n):
    '''
    input: obs: the board
           n: end game start at n empty spaces left 
    '''
    valueMap = [[100, -20, 10, 5, 5, 10, -20, 100],
                [-20, -50, -2, -2, -2, -2, -50, -20],
                [10, -2, -1, -1, -1, -1, -2, 10],
                [5, -2, -1, -1, -1, -1, -2, 5],
                [5, -2, -1, -1, -1, -1, -2, 5],
                [10, -2, -1, -1, -1, -1, -2, 10],
                [-20, -50, -2, -2, -2, -2, -50, -20],
                [100, -20, 10, 5, 5, 10, -20, 100]]
    s = 0

    # if near the end of the game -> optimize stone amount
    simple_s = 0 # let all squares have same value -> just get stone amount
    empty = 0
    for i in range(8):
        for j in range(8):
            
            # Static score
            s += valueMap[i][j] * obs[i*8+j]
            # Endgame stone count
            simple_s += obs[i*8+j]
            # empty spaces
            if obs[i*8+j] == 0:
                empty += 1

    if empty <= 5:
        return simple_s * 16

    return s+random()

def posEval(obs):
    '''
    A simple sum of value for every tile.
    Should be good enough for testing.
    Took from: 
    Reinforcement Learning and its Application to Othello.
    by Nees Jan van Eck, Michiel van Wezel
    '''
    valueMap = [[100, -20, 10, 5, 5, 10, -20, 100],
                [-20, -50, -2, -2, -2, -2, -50, -20],
                [10, -2, -1, -1, -1, -1, -2, 10],
                [5, -2, -1, -1, -1, -1, -2, 5],
                [5, -2, -1, -1, -1, -1, -2, 5],
                [10, -2, -1, -1, -1, -1, -2, 10],
                [-20, -50, -2, -2, -2, -2, -50, -20],
                [100, -20, 10, 5, 5, 10, -20, 100]]
    s = 0
    for i in range(8):
        for j in range(8):            
            s += valueMap[i][j] * obs[i*8+j]
    return s+random()

def enhancedPosEval(obs):
    valueMap = [[100, -20, 10, 5, 5, 10, -20, 100],
                [-20, -50, -2, -2, -2, -2, -50, -20],
                [10, -2, -1, -1, -1, -1, -2, 10],
                [5, -2, -1, -1, -1, -1, -2, 5],
                [5, -2, -1, -1, -1, -1, -2, 5],
                [10, -2, -1, -1, -1, -1, -2, 10],
                [-20, -50, -2, -2, -2, -2, -50, -20],
                [100, -20, 10, 5, 5, 10, -20, 100]]
    s = 0
    liberty = 0
    direct = [(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    if obs[0][0]:
        valueMap[0][1] = 0
        valueMap[1][1] = 0
        valueMap[1][0] = 0
    if obs[7][0]:
        valueMap[7][1] = 0
        valueMap[6][1] = 0
        valueMap[6][0] = 0
    if obs[0][7]:
        valueMap[0][6] = 0
        valueMap[1][6] = 0
        valueMap[1][7] = 0
    if obs[7][7]:
        valueMap[7][6] = 0
        valueMap[6][6] = 0
        valueMap[6][7] = 0
        
    for i in range(8):
        for j in range(8):
            # static score
            s += valueMap[i][j] * obs[i*8+j]
            # liberty: difference empty space adjacent of two colors
            if obs[i][j] == 0:
                for d in direct:
                    if 0<=i+d[0]<8 and 0<=j+d[1]<8:
                        liberty += obs[i+d[0]][j+d[1]]
    
    # TODO: edge/corner bonus

    return s + bonus*bonusFactor - liberty * libertyFactor