import os
import time

from agent.GWFrank_func.match_agents import matchup, matchup_mp, playgame
from agent.GWFrank_func.test_agent_class import MinimaxCountTestAgent, LittleRandomTestAgent, RandomTestAgent
from agent.GWFrank_func.eval_funcs import posEval, posEvalEndgameVariation

if __name__ == "__main__": # Don't delete this line, it's needed for mp to work
    # start = time.time() # timer
    rounds = 50
    depth = 5
    core_cnt = os.cpu_count()//2
    # core_cnt = 4
    
    agents = [
              LittleRandomTestAgent(posEvalEndgameVariation, depth, 0.03),
              RandomTestAgent(),
              MinimaxCountTestAgent(posEvalEndgameVariation, depth),
             ]
    agent_num = 2
    agent1 = agents[1]
    agent2 = agents[2]

    matchup_mp(agent1, agent2, rounds, core_cnt)
    # matchup(agent1, agent2, rounds)

    print("="*20)
    print(f"In {rounds*2} games...")
    for a in [agent1, agent2]:
        W, L, D = a.win, a.loss, a.draw
        name = a.agent_name()
        print(f"{name} has record {W}-{L}-{D}")
    print("="*20)

    # end = time.time() # timer
    # print(f"test finish in {end-start:.2f}s") # timer