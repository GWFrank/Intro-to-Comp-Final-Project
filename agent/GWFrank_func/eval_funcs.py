from random import random
def posEvalEndgameVariation(obs):
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
    simple_s = 0 # let all squares have same value -> just get stone amount
    empty = 0
    for i in range(8):
        for j in range(8):
            
            s += valueMap[i][j] * obs[i*8+j]
            simple_s += obs[i*8+j]
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
    simple_s = 0 # let all squares have same value -> just get stone amount
    empty = 0
    for i in range(8):
        for j in range(8):
            
            s += valueMap[i][j] * obs[i*8+j]
    return s+random()