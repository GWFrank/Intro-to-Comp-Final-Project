from .make_move import makeMove

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

def playgame(first_agent, second_agent):
    """Let two agents play a game.
    Args:
        first_agent: the one that goes first
        second_agent: the one that goes second
    
    Returns:
        list: the board at end-game state
    """
    first_agent.color = -1
    second_agent.color = 1
    agents = {-1: first_agent, 1: second_agent}
    
    board = [ 0,  0,  0,  0,  0,  0,  0,  0,
              0,  0,  0,  0,  0,  0,  0,  0,
              0,  0,  0,  0,  0,  0,  0,  0,
              0,  0,  0,  1, -1,  0,  0,  0,
              0,  0,  0, -1,  1,  0,  0,  0,
              0,  0,  0,  0,  0,  0,  0,  0,
              0,  0,  0,  0,  0,  0,  0,  0,
              0,  0,  0,  0,  0,  0,  0,  0 ]
    color = -1
    nomovecount = 0
    while nomovecount <= 2:
        try:
            move = agents[color].play(board)
            board = makeMove(board, move, color)
            nomovecount = 0
        except:
            nomovecount += 1
            pass
        color = -color
    
    return board

def matchup(agent1, agent2, rounds=10):
    """Let two agents play against each other many times.
    Args:
        agent1
        agent2
        rounds (int): how many rounds of game (each going first)
    
    Returns:
        tuple: ((agent1.s_depth, agent1_wins), (agent2.s_depth, agent2_wins), draws)
    """
    agent1_w = 0
    agent2_w = 0
    draw = 0
    
    # agent 1 go first as black
    for _ in range(rounds):
        board = playgame(agent1, agent2)
        game_result = sum(board)
        if game_result > 0:
            agent2_w += 1
        elif game_result < 0:
            agent1_w += 1
        elif game_result == 0:
            draw += 1
    
    # agent 2 go first as black
    for _ in range(rounds):
        board = playgame(agent2, agent1)
        game_result = sum(board)
        if game_result > 0:
            agent1_w += 1
        elif game_result < 0:
            agent2_w += 1
        elif game_result == 0:
            draw += 1
    
    agent1.win += agent1_w
    agent1.loss += agent2_w
    agent1.draw += draw

    agent2.win += agent2_w
    agent2.loss += agent1_w
    agent2.draw += draw

    return ((agent1.s_depth, agent1_w), (agent2.s_depth, agent2_w), draw)