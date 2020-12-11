from agent.GWFrank_func.match_agents import matchup
from agent.GWFrank_func.test_agent_class import MinimaxTestAgent, LittleRandomTestAgent
from agent.GWFrank_func.eval_funcs import posEval, posEvalEndgameVariation

rounds = 100
depth = 4
agents = [LittleRandomTestAgent(posEvalEndgameVariation, depth, 0.03),
          MinimaxTestAgent(posEvalEndgameVariation, depth)]
agent_num = len(agents)

for a in range(agent_num):
    for b in range(agent_num):
        if a >= b:
            continue
        matchup(agents[a], agents[b], rounds)

print("="*20)
print(f"In {rounds*(agent_num)*(agent_num-1)} games...")
for a in agents:
    W, L, D = a.win, a.loss, a.draw
    rule, depth = a.rule, a.s_depth
    print(f"{rule} with depth {depth} has record {W}-{L}-{D}")
print("="*20)