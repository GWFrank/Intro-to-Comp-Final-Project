from random import random

from .minimax import minimax_adj, minimax_color
from .random_move import randomMove

class BasicTestAgent:
    def __init__(self):
        self.color = None # int
        self.win, self.loss, self.draw = 0, 0, 0
        self.rule = None

class RandomTestAgent(BasicTestAgent):
    def __init__(self):
        super().__init__()
        self.rule = "random"
    
    def play(self, obs):
        mv = randomMove(obs, self.color)
        return mv

    def agent_name(self):
        return f"{self.rule} agent"

class MinimaxTestAgent(BasicTestAgent):
    def __init__(self, eval_func, s_depth):
        super().__init__()
        self.rule = "pure minimax"
        self.eval_func = eval_func # function
        self.s_depth = s_depth # int
    
    def play(self, obs):
        mv, _ = minimax_adj(obs, self.color, self.s_depth
                            , -float("inf"), float("inf"), self.eval_func)
        return mv
    
    def agent_name(self):
        return f"{self.rule} agent @d={self.s_depth}"

class LittleRandomTestAgent(BasicTestAgent):
    def __init__(self, eval_func, s_depth, random_prob):
        super().__init__()
        self.rule = "minimax + random"
        self.eval_func = eval_func # function
        self.s_depth = s_depth # int
        self.random_prob = random_prob
    
    def play(self, obs):
        p = random()
        if p > self.random_prob:
            mv, _ = minimax_adj(obs, self.color, self.s_depth
                                , -float("inf"), float("inf"), self.eval_func)
        else:
            mv = randomMove(obs, self.color)
        return mv
    
    def agent_name(self):
        return f"{self.rule} agent @d={self.s_depth}"


class PaperTestAgent(BasicTestAgent):
    def __init__(self, eval_func, s_depth):
        super().__init__()
        self.rule = "Paper minimax"
        self.eval_func = eval_func  # function
        self.s_depth = s_depth  # int

    def play(self, obs):
        mv, _ = minimax_color(obs, self.color, self.s_depth, -
                            float("inf"), float("inf"), self.eval_func)
        return mv

    def agent_name(self):
        return f"{self.rule} agent @d={self.s_depth}"
