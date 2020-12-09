from random import choice
import time
import json

from agent.GWFrank_func.zobrist_hash import initHash

# board = [0,  0,  0,  0,  0,  0,  0,  0,
#          0,  0,  0,  0,  0,  0,  0,  0,
#          0,  0,  0,  0,  0,  0,  0,  0,
#          0,  0,  0,  1, -1,  0,  0,  0,
#          0,  0,  0, -1,  1,  0,  0,  0,
#          0,  0,  0,  0,  0,  0,  0,  0,
#          0,  0,  0,  0,  0,  0,  0,  0,
#          0,  0,  0,  0,  0,  0,  0,  0]

start = time.time()
    
with open("agent/GWFrank_func/bitstr.json", "r") as f:
    bitstrs = json.load(f)

for i in range(100000):
    board = []
    for _ in range(64):
        board.append(choice([-1, 0, 1]))

    my_hash = initHash(board, bitstrs)

    # print(bin(my_hash)[2:])
end = time.time()
print(f"hashing finish in {end-start:.3f}s")