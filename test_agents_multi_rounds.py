import os
import time
import pickle

from agent.GWFrank_func.match_agents import matchup, matchup_mp, playgame
from agent.GWFrank_func.test_agent_class import MinimaxTestAgent, LittleRandomTestAgent, RandomTestAgent, NEATAgent
from agent.GWFrank_func.eval_funcs import posEval, posEvalEndgameVariation

nn_file_path = "agent/GWFrank_func/best_trained_with_randomagent.pickle"
with open(nn_file_path, "rb") as f:
    nn = pickle.load(f)

if __name__ == "__main__": # Don't delete this line, it's needed for mp to work
    start = time.time() # timer
    rounds = 50
    depth = 4
    core_cnt = os.cpu_count()//2
    # core_cnt = 2
    
    agents = [
              LittleRandomTestAgent(posEvalEndgameVariation, depth, 0.03),
              MinimaxTestAgent(posEvalEndgameVariation, depth),
              RandomTestAgent(),
              NEATAgent(nn, depth, 1)
             ]
    agent_num = 2
    agent1 = agents[0]
    agent2 = agents[3]

    matchup_mp(agent1, agent2, rounds, core_cnt)
    # matchup(agent1, agent2, rounds)

    print("="*20)
    print(f"In {rounds*2} games...")
    for a in [agent1, agent2]:
        W, L, D = a.win, a.loss, a.draw
        name = a.agent_name()
        print(f"{name} has record {W}-{L}-{D}")
    print("="*20)

    end = time.time() # timer
    print(f"test finish in {end-start:.2f}s") # timer