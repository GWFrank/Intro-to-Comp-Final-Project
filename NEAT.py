import os
import neat
import multiprocessing as mp
import pickle

from agent.GWFrank_func.match_agents import matchup, matchup_mp, playgame
from agent.GWFrank_func.test_agent_class import MinimaxTestAgent, LittleRandomTestAgent, RandomTestAgent, NEATAgent
from agent.GWFrank_func.eval_funcs import posEval, posEvalEndgameVariation

# target_agent = MinimaxTestAgent(posEvalEndgameVariation, 2)
# target_agent = LittleRandomTestAgent(posEvalEndgameVariation, 2, 1/32)
# target_agent = RandomTestAgent()

generation = 0
process_num = 2

def eval_genomes(genome, config):
    global generation
    generation += 1
    
    agents = []
    ge = []
    networks = []

    for _, g in genome:
        g.fitness = 0
        network = neat.nn.FeedForwardNetwork.create(g, config)
        networks.append(network)
        agents.append(NEATAgent(network, 1, generation))
        ge.append(g)
    
    records = dict()

    pool = mp.Pool(process_num)
    args = []

    for x, agent_1 in enumerate(agents):
        records[id(agent_1)] = 0
        for y, agent_2 in enumerate(agents):
            if x >= y:
                continue
            args.append((agent_1, agent_2, 1))

    results = pool.starmap(matchup, args)
    pool.close()
    pool.join()

    for r in results:
        records[r[0][0]] += 3*r[0][1] + r[2][0]
        records[r[1][0]] += 3*r[1][1] + r[2][0]

    for idx, agent in enumerate(agents):
        point = records[id(agent)]
        ge[idx].fitness = point

    # for idx, agent in enumerate(agents):
    #     win_rate = matchup_mp(agent, target_agent, 50, process_num)
    #     ge[idx].fitness = 2*(win_rate-0.5)
    #     print(f"{idx:2} win rate: {win_rate} | fitness: {2*(win_rate-0.5)}")
    #     print(networks[idx])
    # print("="*20)



def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
    
    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(eval_genomes, 10)
    print(f'\nBest genome:\n{winner}')

    network = neat.nn.FeedForwardNetwork.create(winner, config)
    pickle.dump(network,open("best.pickle", "wb"))


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "NEAT_config.txt")
    run(config_path)



