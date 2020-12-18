import os
import time
import pickle


from agent.GWFrank_func.match_agents import matchup, matchup_mp, playgame
from agent.GWFrank_func.test_agent_class import RandomTestAgent, MinimaxCountTestAgent, PaperTestAgent
from agent.GWFrank_func.test_agent_class import MinimaxTestAgent, LittleRandomTestAgent, MinimaxModTestAgent
from agent.GWFrank_func.test_agent_class import NEATTestAgent, NEATModTestAgent
from agent.GWFrank_func.eval_funcs import posEval, posEvalEndgameVariation, enhancedPosEval


RTA = RandomTestAgent
MTA = MinimaxTestAgent
LRTA = LittleRandomTestAgent
MMTA = MinimaxModTestAgent
NTA = NEATTestAgent
NMTA = NEATModTestAgent
MCTA = MinimaxCountTestAgent
PTA = PaperTestAgent

nn_file_path = "agent/GWFrank_func/best_trained_with_randomagent.pickle"
with open(nn_file_path, "rb") as f:
    nn = pickle.load(f)


if __name__ == "__main__": # Don't delete this line, it's needed for mp to work
    # start = time.time() # timer
    
    rounds = 10
    core_cnt = os.cpu_count()//2
    # core_cnt = 20
    balanced = True

    depth = 4
    random_step = 4

    random_agent = RTA()
    basic_mm_agent = MTA(posEvalEndgameVariation, depth)
    random_mm_agent = LRTA(posEvalEndgameVariation, depth, 0.03)
    neat_mm_agent = NTA(nn, depth)
    mod_mm_agent = MMTA(posEvalEndgameVariation, depth, random_step)
    mod_neat_agent = NMTA(nn, depth, random_step)
    mm_cnt_agent = MCTA(posEvalEndgameVariation, depth)
    paper_mm_agent = PTA(enhancedPosEval, depth)

    
    agent1 = random_agent
    agent2 = paper_mm_agent

    matchup_mp(agent1, agent2, rounds, core_cnt, balanced)
    # matchup(agent1, agent2, rounds)

    print("="*20)
    for a in [agent1, agent2]:
        W, L, D = a.win, a.loss, a.draw
        name = a.agent_name()
        print(f"{name} has record {W}-{L}-{D}")
    print("="*20)

    # end = time.time() # timer
    # print(f"test finish in {end-start:.2f}s") # timer