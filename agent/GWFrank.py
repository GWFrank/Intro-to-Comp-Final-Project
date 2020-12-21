import random
import sys
import pickle

import pygame
from pygame.constants import MOUSEBUTTONDOWN, MOUSEMOTION

from agent.GWFrank_func.minimax import minimax, minimax_adj
from agent.GWFrank_func.random_move import randomMove
from agent.GWFrank_func.eval_funcs import posEval, posEvalEndgameVariation

class BaseAgent():
    def __init__(self, color = "black", rows_n = 8, cols_n = 8, width = 600, height = 600):
        self.color = color
        self.rows_n = rows_n
        self.cols_n = cols_n
        self.block_len = 0.8 * min(height, width)/cols_n
        self.col_offset = (width - height)/2 + 0.1 * min(height, width) + 0.5 * self.block_len
        self.row_offset = 0.1 * min(height, width) + 0.5 * self.block_len
        

    def step(self, reward, obs):
        """
        Parameters
        ----------
        reward : dict
            current_score - previous_score
            
            key: -1(black), 1(white)
            value: numbers
            
        obs    :  dict 
            board status

            key: int 0 ~ 63
            value: [-1, 0 ,1]
                    -1 : black
                     0 : empty
                     1 : white

        Returns
        -------
        tuple:
            (x, y) represents position, where (0, 0) mean top left. 
                x: go right
                y: go down
        event_type:
            non human agent uses pygame.USEREVENT
        """

        raise NotImplementError("You didn't finish your step function. Please override step function of BaseAgent!")


class BetterRandomAgent(BaseAgent):
    def step(self, reward, obs):
        obs = list(obs.values())
        if self.color == "black":
            c = -1
        else:
            c = 1
        
        mv = randomMove(obs, c)

        x = self.col_offset + (mv%8)  * self.block_len
        y = self.row_offset + (mv//8) * self.block_len
        return (x, y), pygame.USEREVENT

# =======================================================
with open("agent/GWFrank_func/best_trained_with_randomagent.pickle", "rb") as f:
    NN = pickle.load(f)

DEPTH = 5
RANDOM_STEPS = 2
RANDOM_PROB = 0.03
# =======================================================

class BasicMinimaxAgent(BaseAgent):
    def step(self, reward, obs):
        global DEPTH, RANDOM_STEPS, RANDOM_PROB
        obs = list(obs.values())
        if self.color == "black":
            c = -1
        else:
            c = 1
        
        if (64-obs.count(0))//2 < RANDOM_STEPS:
            mv = randomMove(obs, c)
        else:
            mv, _ = minimax_adj(obs, c, DEPTH
                                , -float('inf'), float('inf'), posEvalEndgameVariation)

        x = self.col_offset + (mv%8)  * self.block_len
        y = self.row_offset + (mv//8) * self.block_len
        return (x, y), pygame.USEREVENT


class LittleRandomAgent(BaseAgent):
    def step(self, reward, obs):
        global DEPTH, RANDOM_STEPS, RANDOM_PROB
        obs = list(obs.values())
        if self.color == "black":
            c = -1
        else:
            c = 1
        
        p = random.random()
        if p > RANDOM_PROB:
            mv, _ = minimax_adj(obs, c, DEPTH
                                , -float('inf'), float('inf'), posEvalEndgameVariation)
        else:
            mv = randomMove(obs, c)
        
        x = self.col_offset + (mv%8)  * self.block_len
        y = self.row_offset + (mv//8) * self.block_len
        return (x, y), pygame.USEREVENT


class NEATAgent(BaseAgent):
    def eval(self, obs):
        global NN
        return NN.activate(tuple(obs))[0]

    def step(self, reward, obs):
        global DEPTH, RANDOM_STEPS, RANDOM_PROB
        obs = list(obs.values())
        if self.color == "black":
            c = -1
        else:
            c = 1
        
        if (64-obs.count(0))//2 < RANDOM_STEPS:
            mv = randomMove(obs, c)
        else:
            mv, _ = minimax_adj(obs, c, DEPTH, -float('inf'), float('inf'), self.eval)

        x = self.col_offset + (mv%8)  * self.block_len
        y = self.row_offset + (mv//8) * self.block_len
        return (x, y), pygame.USEREVENT


class MyAgent(NEATAgent):
    pass
