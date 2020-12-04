import random
import pygame
import sys
from pygame.constants import MOUSEBUTTONDOWN, MOUSEMOTION

from agent.our_functions.minimax import minimax
from agent.our_functions.random_move import randomMove

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
    

class MyAgent(BaseAgent):
    # what are you doing step function?
    def step(self, reward, obs):
        # board = [obs[8*row:8*row+8] for row in range(8)]
        
        obs = list(obs.values())
        if self.color == "black":
            c = -1
        else:
            c = 1
        
        mv, _ = minimax(obs, c, 4)

        x = self.col_offset + mv[0]*self.block_len
        y = self.row_offset + mv[1]*self.block_len
        
        return (x, y), pygame.USEREVENT

class BetterRandomAgent(BaseAgent):
    def step(self, reward, obs):
        if self.color == "black":
            c = -1
        else:
            c = 1
        mv = randomMove(obs, c)
        x = self.col_offset + mv[0]*self.block_len
        y = self.row_offset + mv[1]*self.block_len
        return (x, y), pygame.USEREVENT
