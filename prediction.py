from agents import Q_learningAgent
from gridworld import GridWorld
import numpy as np

agent = Q_learningAgent()
env = GridWorld(False)
agent.q_table = np.load("frozen_lake_rl_implementation/q_table.npy")
if __name__ == '__main__': 
    done = False
    
    print("**************Game starts **************************")
    env.render()
    while not done: 
        state = env.get_state()
        action = np.argmax(agent.q_table[state[0],state[1]])
        next_state, reward, done = env.step(action)
        print()
        env.render()

        if done:
            print("**************Game over **************************")
            break