import multiprocessing as mp

from agent.GWFrank_func.match_agents import matchup, matchup_mp, playgame
from agent.GWFrank_func.test_agent_class import MinimaxTestAgent, LittleRandomTestAgent, RandomTestAgent
from agent.GWFrank_func.eval_funcs import posEval, posEvalEndgameVariation

if __name__ == "__main__":

    rounds = 50
    depth = 4
    process_num = 4
    
    agents = [
              LittleRandomTestAgent(posEvalEndgameVariation, depth, 0.03),
            #   MinimaxTestAgent(posEvalEndgameVariation, depth),
              RandomTestAgent(),
             ]
    agent_num = len(agents)
    agent1 = agents[0]
    agent2 = agents[1]

    # agent_num = 2

    # for a in range(agent_num):
    #     for b in range(agent_num):
    #         if a >= b:
    #             continue
    #         matchup(agents[a], agents[b], rounds)

    # =====================================================
    agent1_w = 0
    agent2_w = 0
    draw = 0

    # agent 1 go first as black
    pool = mp.Pool(process_num)

    args = [(agent1, agent2) for _ in range(rounds)]
    game_results = pool.starmap(playgame, args)

    pool.close()
    pool.join()

    for r in game_results:
        if r > 0:
            agent2_w += 1
        elif r < 0:
            agent1_w += 1
        elif r == 0:
            draw += 1

    # agent 2 go first as black
    pool = mp.Pool(process_num)

    args = [(agent2, agent1) for _ in range(rounds)]
    game_results = pool.starmap(playgame, args)

    pool.close()
    pool.join()

    for r in game_results:
        if r > 0:
            agent1_w += 1
        elif r < 0:
            agent2_w += 1
        elif r == 0:
            draw += 1

    agent1.win += agent1_w
    agent1.loss += agent2_w
    agent1.draw += draw

    agent2.win += agent2_w
    agent2.loss += agent1_w
    agent2.draw += draw
    # =====================================================

    print("="*20)
    print(f"In {rounds*2} games...")
    for a in agents:
        W, L, D = a.win, a.loss, a.draw
        name = a.agent_name()
        print(f"{name} has record {W}-{L}-{D}")
    print("="*20)