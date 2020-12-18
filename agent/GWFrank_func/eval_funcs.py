from random import random
def posEvalEndgameVariation(obs):
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

def enhancedPosEval(obs, color):
    valueMap = [[500, -86, 96, 26, 26, 96, -86, 500],
                [-86, -1219, -6, 0, 0, -6, -1219, -86],
                [96, -6, 52, 15, 15, 52, -6, 96],
                [26, 0, 15, -17, -17, 15, 0, 26],
                [26, 0, 15, -17, -17, 15, 0, 26],
                [96, -6, 52, 15, 15, 52, -6, 96],
                [-86, -1219, -6, 0, 0, -6, -1219, -86],
                [500, -86, 96, 26, 26, 96, -86, 500]]
    s = 0
    liberty = 0
    # change tiles around corner to 0 if corner is taken
    direct = [(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    if obs[0]:
        valueMap[0][1] = 0
        valueMap[1][1] = 0
        valueMap[1][0] = 0
    if obs[56]:
        valueMap[7][1] = 0
        valueMap[6][1] = 0
        valueMap[6][0] = 0
    if obs[7]:
        valueMap[0][6] = 0
        valueMap[1][6] = 0
        valueMap[1][7] = 0
    if obs[63]:
        valueMap[7][6] = 0
        valueMap[6][6] = 0
        valueMap[6][7] = 0
        
    for i in range(8):
        for j in range(8):
            # static score
            s += valueMap[i][j] * obs[i*8+j]
            # liberty: difference empty space adjacent of two colors
            if obs[i*8+j] == 0:
                for d in direct:
                    if 0<=i+d[0]<8 and 0<=j+d[1]<8:
                        liberty += obs[ (i+d[0])*8+j+d[1] ]
    
    # TODO: edge/corner bonus
    bonusRecord = [0 for _ in range(64)]
    if obs[0] == color:
        for i in range(8): # right
            if obs[i*8] == color:
                bonusRecord[i*8] = 1
            else: break
        for i in range(8): # down
            if obs[i] == color:
                bonusRecord[i] = 1
            else: break
    if obs[7] == color:
        for i in range(8): # right
            if obs[i*8+7] == color:
                bonusRecord[i*8+7] = 1
            else: break
        for i in range(8): # up
            if obs[7-i] == color:
                bonusRecord[7-i] = 1
            else: break
    if obs[56] == color:
        for i in range(8): # left
            if obs[(7-i)*8] == color:
                bonusRecord[(7-i)*8] = 1
            else: break
        for i in range(8): # down
            if obs[56+i] == color:
                bonusRecord[56+i] = 1
            else: break
    if obs[63] == color:
        for i in range(8): # left
            if obs[(7-i)*8+7] == color:
                bonusRecord[(7-i)*8+7] = 1
            else: break
        for i in range(8): # up
            if obs[7*8+7-i] == color:
                bonusRecord[7*8+7-i] = 1
            else: break

    return s + sum(bonusRecord)*26*color - liberty * 104 * color
