import numpy as np
from agents import Q_learningAgent, Deep_Q_learningAgent
from gridworld import GridWorld
import random

env = GridWorld(True)
deep_agent = Deep_Q_learningAgent()

max_episodes = 100000
episode = 0
replay_memory = []
q_network = deep_agent# initialize network with random weights
q_target_network = q_network# initalize target network with weights the same as q network 
batch_size = 20
count = 0
for episode in range(max_episodes):
    # sampling 
    env.reset()
    encoded_grid_actual_step = q_network.encoding_input(env.grid)
    done_sampling = False
    while done_sampling is not True:
        action = q_network.choose_action(env)
        next_step, reward, done_sampling = env.step(action)
        grid_next_step = env.grid
        encoded_grid_next_step = q_network.encoding_input(grid_next_step)
        replay_memory.append([encoded_grid_actual_step,action,reward,encoded_grid_next_step,done_sampling])

        if len(replay_memory) > batch_size:
            count += 1
            # sample random minibatch of transitions
            encoded_grid_actual_steps, actions, rewards, encoded_grid_next_steps, dones= random.sample(replay_memory,batch_size)
            for j in range(batch_size):
                if dones[j]==True:
                    best_target_action= np.max(q_target_network.network(encoded_grid_next_steps[j]))
                    q_target_value = rewards[j] + q_target_network.gamma * best_target_action
                else: 
                    q_target_value = rewards[j]
                
                # q current network value
                q_current_action_values = q_network.network(encoded_grid_actual_steps[j])
                q_network.criterion(q_target_value,q_current_action_values[action])
        else:
            continue

        deep_agent.epsilon = max(0.01, np.exp(-0.001 * episode))
        print(deep_agent.epsilon)
        if count == 2000:
            q_target_network = q_network
            count = 0


        
    





# agent = Q_learningAgent()
# max_episodes = 100000
# episode = 0
# if __name__ == '__main__': 
#     # episodes for the training
#     while episode < max_episodes:
#         agent.epsilon = max(0.01, np.exp(-0.001 * episode))
#         while True: 
#             state = env.get_state()
#             action = agent.choose_action(state)
#             next_step,reward, done = env.step(action)
#             q_value_table = agent.update_q_values(state,reward,next_step,action)
#             print(episode)
#             env.render()
            
#             if done:
#                 env.reset()
#                 episode +=1
#                 break
#     np.save("frozen_lake_rl_implementation/q_table.npy", agent.q_table)