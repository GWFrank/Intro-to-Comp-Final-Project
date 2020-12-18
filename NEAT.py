import os
import neat
import multiprocessing as mp
import pickle

from agent.GWFrank_func.match_agents import matchup_training
from agent.GWFrank_func.test_agent_class import *
from agent.GWFrank_func.eval_funcs import posEval, posEvalEndgameVariation

nn_file_name = "cool_agent.pickle"

target_agent = MinimaxModTestAgent(posEvalEndgameVariation, 2, 4)
# target_agent = LittleRandomTestAgent(posEvalEndgameVariation, 2, 1/32)
# target_agent = RandomTestAgent()

# generation = 0
process_num = 6
rounds_each_eval = 50
random_step = 4
training_gens = 10

def eval_genomes(genome, config):
    # global generation
    # generation += 1
    
    agents = []
    ge = []
    networks = []

    for _, g in genome:
        g.fitness = 0
        network = neat.nn.FeedForwardNetwork.create(g, config)
        networks.append(network)
        agents.append(NEATTrainAgent(network, 1, random_step))
        ge.append(g)
    
    # ================================
    pool = mp.Pool(process_num)

    args = []
    for idx, agent in enumerate(agents):
        args.append((agent, idx, target_agent, rounds_each_eval))
    
    game_results = pool.starmap(matchup_training, args)

    pool.close()
    pool.join()
    # ================================

    for (idx, win_rate) in game_results:
        ge[idx].fitness = win_rate




def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
    
    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(eval_genomes, training_gens)

    print(f'\nBest genome:\n{winner}')

    network = neat.nn.FeedForwardNetwork.create(winner, config)
    pickle.dump(network,open(nn_file_name, "wb"))


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "NEAT_config.txt")
    run(config_path)



