import multiprocessing as mp
import time

from agent.GWFrank_func.match_agents import matchup
from agent.GWFrank_func.test_agent_class import MinimaxTestAgent
from agent.GWFrank_func.eval_funcs import positionalEval


if __name__ == "__main__":
    rounds = 1
    max_d = 5
    process_num = 4

    pos_agents = [MinimaxTestAgent(positionalEval, d) for d in range(1, max_d+1)]
    tot_win = [0 for _ in range(max_d)]
    tot_draw = 0

    pool = mp.Pool(process_num)
    args = []

    for a in range(max_d):
        for b in range(max_d):
            if a <= b:
                continue
            args.append((pos_agents[a], pos_agents[b], rounds))
    
    result = pool.starmap(matchup, args)
    pool.close()
    pool.join()

    for r in result:
        tot_win[r[0][0]-1] += r[0][1]
        tot_win[r[1][0]-1] += r[1][1]
        tot_draw += r[2]

    print("="*20)
    print(f"In {rounds*2*(max_d-1)} games...")
    for d in range(max_d):
        print(f"Depth {d+1} wins {tot_win[d]} ({tot_win[d]/(rounds*2*(max_d-1)):.2f})")
    print(f"Draw happens {tot_draw} times")
    print("="*20)

    # print("="*20)
    # print(f"In {rounds*2*(max_d-1)} games...")
    # for a in pos_agents:
    #     W, L, D = a.win, a.loss, a.draw
    #     rule, depth = a.rule, a.s_depth
    #     print(f"{rule} with depth {depth} has record {W}-{L}-{D}")
    # print("="*20)
