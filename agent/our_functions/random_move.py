from .available_spot import getAvailableSpot
from random import choice

def randomMove(obs, color):
    possible_moves = list(getAvailableSpot(obs, color))
    return choice(possible_moves)