from random import choice
import time
import json

from agent.GWFrank_func.zobrist_hash import initHash, updateHash

with open("agent/GWFrank_func/bitstr.json", "r") as f:
    bitstrs = json.load(f)

start = time.time()

prev_board = [0,  0,  0,  0,  0,  0,  0,  0,
         0,  0,  0,  0,  0,  0,  0,  0,
         0,  0,  0,  0,  0,  0,  0,  0,
         0,  0,  0,  1, -1,  0,  0,  0,
         0,  0,  0, -1,  1,  0,  0,  0,
         0,  0,  0,  0,  0,  0,  0,  0,
         0,  0,  0,  0,  0,  0,  0,  0,
         0,  0,  0,  0,  0,  0,  0,  0]

my_hash = initHash(prev_board, bitstrs)

for i in range(1000):
    board = []
    for _ in range(64):
        board.append(choice([-1, 1]))

    # my_hash = updateHash(my_hash, prev_board, board, bitstrs)
    my_hash = initHash(board, bitstrs)
    
    prev_board = board.copy()

    # print(bin(my_hash)[2:])
end = time.time()
print(f"hashing finish in {end-start:.3f}s")

