from agent.GWFrank_func.match_agents import matchup
from agent.GWFrank_func.test_agent_class import MinimaxTestAgent
from agent.GWFrank_func.eval_funcs import positionalEval

rounds = 1
max_d = 4

pos_agents = [MinimaxTestAgent(positionalEval, d) for d in range(1, max_d+1)]

for a in range(max_d):
    for b in range(max_d):
        if a <= b:
            continue
        matchup(pos_agents[a], pos_agents[b], rounds)

print("="*20)
print(f"In {rounds*2*(max_d-1)} games...")
for a in pos_agents:
    W, L, D = a.win, a.loss, a.draw
    rule, depth = a.rule, a.s_depth
    print(f"{rule} with depth {depth} has record {W}-{L}-{D}")
print("="*20)