from .minimax import minimax_adj
from .make_move import makeMove

class TestAgent:
    def __init__(self, eval_func, s_depth):
        self.eval_func = eval_func # function
        self.color = None # int
        self.s_depth = s_depth # int
    
    def play(self, obs):
        mv, _ = minimax_adj(obs, self.color, self.s_depth, -float("inf"), float("inf"), self.eval_func)
        return mv

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

def matchup(agent1, agent2, rounds=10):
    """Let two agents play against each other
    Args:
        agent1 (class TestAgent)
        agent2 (class TestAgent)
        rounds (int): how many rounds of game (each going first)
    
    Returns:
        tuple: ((agent1.s_depth, agent1_wins), (agent2.s_depth, agent2_wins), draws)
    """
    agent1_w = 0
    agent2_w = 0
    draw = 0
    
    # agent 1 go first as black
    for _ in range(rounds):
        board = [ 0,  0,  0,  0,  0,  0,  0,  0,
                  0,  0,  0,  0,  0,  0,  0,  0,
                  0,  0,  0,  0,  0,  0,  0,  0,
                  0,  0,  0,  1, -1,  0,  0,  0,
                  0,  0,  0, -1,  1,  0,  0,  0,
                  0,  0,  0,  0,  0,  0,  0,  0,
                  0,  0,  0,  0,  0,  0,  0,  0,
                  0,  0,  0,  0,  0,  0,  0,  0 ]
        agent1.color = -1
        agent2.color = 1
        color = -1
        nomovecount = 0
        colorName = {-1: 'agent1', 1: 'agent2'}
        agents = {-1: agent1, 1: agent2}
        while nomovecount <= 2:
            move = agents[color].play(board)
            try:
                # print(f"{colorName[color]} move in {(move%8, move//8)}") # print
                board = makeMove(board, move, color)
                nomovecount = 0
                # printBoard(board) # print
                # print("="*20) # print
            except:
                nomovecount += 1
                pass
            
            color = -color
        
        game_result = sum(board)
        if game_result > 0:
            agent2_w += 1
        elif game_result < 0:
            agent1_w += 1
        elif game_result == 0:
            draw += 1
    
    # agent 2 go first as black
    for _ in range(rounds):
        board = [ 0,  0,  0,  0,  0,  0,  0,  0,
                  0,  0,  0,  0,  0,  0,  0,  0,
                  0,  0,  0,  0,  0,  0,  0,  0,
                  0,  0,  0,  1, -1,  0,  0,  0,
                  0,  0,  0, -1,  1,  0,  0,  0,
                  0,  0,  0,  0,  0,  0,  0,  0,
                  0,  0,  0,  0,  0,  0,  0,  0,
                  0,  0,  0,  0,  0,  0,  0,  0 ]
        agent1.color = 1
        agent2.color = -1
        color = -1
        nomovecount = 0
        colorName = {-1: 'agent2', 1: 'agent1'}
        agents = {-1: agent2, 1: agent1}
        while nomovecount <= 2:
            move = agents[color].play(board)
            try:
                # print(f"{colorName[color]} move in {(move%8, move//8)}") # print
                board = makeMove(board, move, color)
                nomovecount = 0
                # printBoard(board) # print
                # print("="*20) # print
            except:
                nomovecount += 1
                pass
            
            color = -color
        
        game_result = sum(board)
        if game_result > 0:
            agent1_w += 1
        elif game_result < 0:
            agent2_w += 1
        elif game_result == 0:
            draw += 1
    
    # print("="*20)
    # print(f"In {rounds*2} games...")
    # print(f"Agent1 wins {agent1_w} ({agent1_w/(rounds*2)})")
    # print(f"Agent2 wins {agent2_w} ({agent2_w/(rounds*2)})")
    # print(f"Draw happens {draw} times ({draw/(rounds*2)})")
    # print("="*20)
    return ((agent1.s_depth, agent1_w), (agent2.s_depth, agent2_w), draw)