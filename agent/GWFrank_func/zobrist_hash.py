from random import randint
import json

def initHash(board, bitstrs):
    init_hash = 0
    # with open("agent/GWFrank_func/bitstr.json", "r") as f:
    #     bitstrs = json.load(f)
    
    for i in range(64):
        if board[i] != 0:
            init_hash = init_hash^bitstrs[f"{board[i]}{i}"]
    return init_hash

def updateHash(brd_hash, old_board, new_board, bitstrs):
    """
    Args:
        brd_hash (int): board's previous hash
        old_board (list): board's previous state
        new_board (list): board's current state
        bitstrs (dict): the bitstrings used to hash in the beginning    
    Returns:
        int : board's new hash
    """
    for i in range(64):
        old_piece = old_board[i]
        new_piece = new_board[i]
        if old_piece != new_piece:
            if old_piece == 0:
                brd_hash = brd_hash^bitstrs[f"{new_piece}{i}"]
            else:
                brd_hash = brd_hash^bitstrs[f"{old_piece}{i}"]^bitstrs[f"{new_piece}{i}"]
    
    return brd_hash