import os
import time
import pickle


from agent.GWFrank_func.match_agents import matchup, matchup_mp, playgame
from agent.GWFrank_func.test_agent_class import RandomTestAgent
from agent.GWFrank_func.test_agent_class import MinimaxTestAgent, LittleRandomTestAgent, MinimaxModTestAgent
from agent.GWFrank_func.test_agent_class import NEATTestAgent, NEATModTestAgent
from agent.GWFrank_func.eval_funcs import posEval, posEvalEndgameVariation


RTA = RandomTestAgent
MTA = MinimaxTestAgent
LRTA = LittleRandomTestAgent
MMTA = MinimaxModTestAgent
NTA = NEATTestAgent
NMTA = NEATModTestAgent


nn_file_path = "agent/GWFrank_func/best_trained_with_randomagent.pickle"
with open(nn_file_path, "rb") as f:
    nn = pickle.load(f)


if __name__ == "__main__": # Don't delete this line, it's needed for mp to work
    # start = time.time() # timer
    
    rounds = 50
    core_cnt = os.cpu_count()//2
    # core_cnt = 20
    
    depth = 4
    random_step = 4

    random_agent = RTA()
    basic_mm_agent = MTA(posEvalEndgameVariation, depth)
    random_mm_agent = LRTA(posEvalEndgameVariation, depth, 0.03)
    neat_mm_agent = NTA(nn, depth, 1)
    mod_mm_agent = MMTA(posEvalEndgameVariation, depth, random_step)
    mod_neat_agent = NMTA(nn, depth, 1, random_step)

    agent_num = 2
    agent1 = mod_mm_agent
    agent2 = mod_neat_agent

    matchup_mp(agent1, agent2, rounds, core_cnt, True)

    print("="*20)
    for a in [agent1, agent2]:
        W, L, D = a.win, a.loss, a.draw
        name = a.agent_name()
        print(f"{name} has record {W}-{L}-{D}")
    print("="*20)

    # end = time.time() # timer
    # print(f"test finish in {end-start:.2f}s") # timer