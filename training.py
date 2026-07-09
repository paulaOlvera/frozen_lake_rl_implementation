import numpy as np
from agent import Agent
from gridworld import GridWorld

if __name__ == "__main__":
    env = GridWorld()
    agent = Agent()
    max_episodes = 100000
    episode = 0
    
    # episodes for the training
    while episode < max_episodes:
        agent.epsilon = max(0.01, np.exp(-0.001 * episode))
        while True: 
            state = env.get_state()
            action = agent.choose_action(state)
            next_step,reward, done = env.step(action)
            agent.update_q_values(state,reward,next_step,action)
            env.render()
            if done:
                env.reset(False)
                episode +=1
                break