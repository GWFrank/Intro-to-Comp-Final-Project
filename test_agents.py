from agent.our_functions.match_agents import matchup, TestAgent
from agent.our_functions.eval_funcs import positionalEval

rounds = 1
max_d = 7

pos_agents = [TestAgent(positionalEval, d) for d in range(1, max_d+1)]
tot_win = [0 for _ in range(max_d)]
tot_draw = 0

for a in range(max_d):
    for b in range(max_d):
        if a <= b:
            continue
        agent1_w, agent2_w, draw = matchup(pos_agents[a], pos_agents[b], rounds)
        tot_win[a] += agent1_w
        tot_win[b] += agent2_w
        tot_draw += draw

print("="*20)
print(f"In {rounds*2*(max_d-1)} games...")
for d in range(max_d):
    print(f"Depth {d+1} wins {tot_win[d]} ({tot_win[d]/(rounds*2*(max_d-1)):.2f})")
print(f"Draw happens {tot_draw} times")
print("="*20)
