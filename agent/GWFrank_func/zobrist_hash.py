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

def updateHash(brd_hash, changes, bitstrs):
    """
    Args:
        brd_hash (int): board's previous hash
        changes (list): list of changes on the board, each element
                        is a tuple (pos, pre_color, cur_color)
    
    Returns:
        int : board's new hash
    """

    # with open("agent/GWFrank_func/bitstr.json", "r") as f:
    #     bitstrs = json.load(f)
    for ch in changes:
        brd_hash = brd_hash^bitstrs[f"{ch[1]}{ch[0]}"]^bitstrs[f"{ch[2]}{ch[0]}"]

    return brd_hash