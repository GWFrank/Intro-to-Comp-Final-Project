import tensorflow as tf
import numpy as np
import multiprocessing as mp

from agent.GWFrank_func.match_agents import matchup, matchup_mp, playgame
from agent.GWFrank_func.test_agent_class import MinimaxTestAgent, LittleRandomTestAgent, RandomTestAgent
from agent.GWFrank_func.eval_funcs import posEval, posEvalEndgameVariation

# Parameters.
learning_rate = 0.1
training_steps = 10
display_step = 1

#Create dataset
W = tf.Variable(tf.ones(64))
# b = tf.Variable(tf.zeros(64))
def linearEval(obs):
    global W
    obs = np.array(obs)
    return np.dot(W.numpy(), obs)

# Stochastic Gradient Descent Optimizer.
optimizer = tf.optimizers.SGD(learning_rate)

def loss_func(W):
    print("loss_ratio calculating....")
    target_agent = MinimaxTestAgent(posEvalEndgameVariation, 4)
    W_agent = MinimaxTestAgent(linearEval, 4)
    loss_ratio = matchup_mp(target_agent, W_agent, 100)
    print(f"loss ratio is {loss_ratio}")
    return loss_ratio

def run_optimization():
    # Wrap computation inside a GradientTape for automatic differentiation.
    with tf.GradientTape() as g:
        loss = loss_func(W)

    # Compute gradients.
    gradients = g.gradient(loss, [W])
    
    # Update W and b following gradients.
    optimizer.apply_gradients(zip(gradients, [W]))

if __name__ == "__main__":
    for step in range(1, training_steps + 1):
    # Run the optimization to update W and b values.
        run_optimization() 
        # if step % display_step == 0:
        #     pred = linear_regression(X)
        #     loss = mean_square(pred, Y)
        #     print("step: %i, loss: %f, W: %f, b: %f" % (step, loss, W.numpy(), b.numpy()))
