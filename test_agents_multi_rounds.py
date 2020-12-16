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
    # start = time.time() # timer
    rounds = 100
    depth = 4
    core_cnt = os.cpu_count()//2
    # core_cnt = 10
    
    agents = [
              LittleRandomTestAgent(posEvalEndgameVariation, depth, 0.03),
              MinimaxTestAgent(posEvalEndgameVariation, depth),
              RandomTestAgent(),
              NEATAgent(nn, depth, 1)
             ]
    little_random_agent = LittleRandomTestAgent(posEvalEndgameVariation, depth, 0.03)
    basic_minimax_agent = MinimaxTestAgent(posEvalEndgameVariation, depth)
    random_agent = RandomTestAgent()
    agent_num = 2
    agent1 = basic_minimax_agent
    agent2 = random_agent

    matchup_mp(agent1, agent2, rounds, core_cnt, False)

    print("="*20)
    for a in [agent1, agent2]:
        W, L, D = a.win, a.loss, a.draw
        name = a.agent_name()
        print(f"{name} has record {W}-{L}-{D}")
    print("="*20)

    # end = time.time() # timer
    # print(f"test finish in {end-start:.2f}s") # timer