def positionalEval(obs):
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
    return s

def positionalEval2(obs):
    valueMap = [[500, -86, 96, 26, 26, 96, -86, 500],
                [-86, -1219, -6, 0, 0, -6, -1219, -86],
                [96, -6, 52, 15, 15, 52, -6, 96],
                [26, 0, 15, -17, -17, 15, 0, 26],
                [26, 0, 15, -17, -17, 15, 0, 26],
                [96, -6, 52, 15, 15, 52, -6, 96],
                [-86, -1219, -6, 0, 0, -6, -1219, -86],
                [500, -86, 96, 26, 26, 96, -86, 500]]
    s = 0
    for i in range(8):
        for j in range(8):
            s += valueMap[i][j] * obs[i*8+j]
    return s
