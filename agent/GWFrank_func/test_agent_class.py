from random import random

from .minimax import minimax_adj, minimax_color, minimaxCount
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
        self.rule = "basic eval"
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
        self.rule = "basic eval + little random"
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


class MinimaxCountTestAgent(BasicTestAgent):
    def __init__(self, eval_func, s_depth):
        super().__init__()
        self.rule = "pure minimax"
        self.eval_func = eval_func  # function
        self.s_depth = s_depth  # int
        
    def play(self, obs):
        
        mv, _ , count = minimaxCount(obs, self.color, self.s_depth, -
                            float("inf"), float("inf"))
        # print(f'Routes counted = {count}')
        return mv

    def agent_name(self):
        return f"{self.rule} agent @d={self.s_depth}"

class MinimaxModTestAgent(BasicTestAgent):
    def __init__(self, eval_func, s_depth, random_steps):
        super().__init__()
        self.rule = "random first & basic eval"
        self.eval_func = eval_func # function
        self.s_depth = s_depth # int
        self.random_steps = random_steps
    
    def play(self, obs):
        if self.random_steps > 0:
            self.random_steps -= 1
            mv = randomMove(obs, self.color)
        else:
            mv, _ = minimax_adj(obs, self.color, self.s_depth
                                , -float("inf"), float("inf"), self.eval_func)
        return mv
    
    def agent_name(self):
        return f"{self.rule} agent @d={self.s_depth}"

class NEATTestAgent(BasicTestAgent):
    def __init__(self, nn, s_depth):
        super().__init__()
        self.rule = "NEAT eval"
        self.nn = nn
        self.s_depth = s_depth
    
    def eval(self, obs):
        return self.nn.activate(tuple(obs))[0]
    
    def play(self, obs):
        mv, _ = minimax_adj(obs, self.color, self.s_depth
                            , -float("inf"), float("inf"), self.eval)
        return mv
    
    def agent_name(self):
        return f"{self.rule} agent"

class NEATModTestAgent(BasicTestAgent):
    def __init__(self, nn, s_depth, random_steps):
        super().__init__()
        self.rule = "random first & NEAT eval"
        self.nn = nn
        self.s_depth = s_depth
        self.random_steps = random_steps
    
    def eval(self, obs):
        return self.nn.activate(tuple(obs))[0]
    
    def play(self, obs):
        if self.random_steps > 0:
            mv = randomMove(obs, self.color)
            self.random_steps -= 1
        else:
            mv, _ = minimax_adj(obs, self.color, self.s_depth
                                , -float("inf"), float("inf"), self.eval)
        return mv
    
    def agent_name(self):
        return f"{self.rule} agent"

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

class NEATTrainAgent(BasicTestAgent):
    def __init__(self, nn, s_depth, random_steps):
        super().__init__()
        self.rule = "NEAT_Training"
        self.nn = nn
        self.s_depth = s_depth
        self.random_steps = random_steps
    
    def eval(self, obs):
        return self.nn.activate(tuple(obs))[0]
    
    def play(self, obs):
        if (64-obs.count(0))//2 <= self.random_steps:
            mv = randomMove(obs, self.color)
        else:
            mv, _ = minimax_adj(obs, self.color, self.s_depth
                                , -float("inf"), float("inf"), self.eval)
        return mv
    
    def agent_name(self):
        return f"{self.rule} agent"