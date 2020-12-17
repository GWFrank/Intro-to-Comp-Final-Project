from .available_spot import getAvailableSpot
from random import choice

def randomMove(obs, color):
    possible_moves = list(getAvailableSpot(obs, color))
    if possible_moves:
        return choice(possible_moves)
    else:
        return None