import numpy as np
from agents import Deep_Q_learningAgent
from gridworld import GridWorld
import random
import torch 

env = GridWorld(False)
q_network = Deep_Q_learningAgent() # initialize network with random weights
q_target_network = Deep_Q_learningAgent() # initalize target network

max_episodes = 1000
episode = 0
replay_memory = []
memory_capacity = 100
q_target_network.network.load_state_dict(q_network.network.state_dict()) # give the same weights of current network to target network
batch_size = 20
count = 0
for episode in range(max_episodes):
    # sampling 
    env.reset()
    encoded_grid_actual_step = q_network.encoding_input(env.grid)
    done_sampling = False
    episode += 1
    print("The episode is",episode)
    while done_sampling is not True:
        action = q_network.choose_action(env)
        next_step, reward, done_sampling = env.step(action)
        grid_next_step = env.grid
        encoded_grid_next_step = q_network.encoding_input(grid_next_step)
        replay_memory.append([encoded_grid_actual_step,action,reward,encoded_grid_next_step,done_sampling])
        if len(replay_memory) > memory_capacity:
            replay_memory.pop(0)

        encoded_grid_actual_step = encoded_grid_next_step
        losses = []
        if len(replay_memory) > batch_size:
            count += 1
            # sample random minibatch of transitions
            batch = random.sample(replay_memory,batch_size)
            encoded_grid_actual_steps, actions, rewards, encoded_grid_next_steps, dones = zip(*batch)
            for j in range(batch_size):
                if dones[j]:
                    q_target_value = rewards[j]
                else: 
                    best_target_action= max(q_target_network.network(encoded_grid_next_steps[j]))
                    q_target_value = rewards[j] + q_target_network.gamma * best_target_action
                q_target_value = torch.tensor(q_target_value,dtype=torch.float32)
                # q current network value
                q_current_action_values = q_network.network(encoded_grid_actual_steps[j])
                loss = q_network.criterion(q_target_value,q_current_action_values[actions[j]])
                losses.append(loss)
                
            loss = torch.stack(losses).mean()
            q_network.optimizer.zero_grad()
            loss.backward()
            q_network.optimizer.step()
        else:
            continue

        q_network.epsilon = max(0.01, np.exp(-0.001 * episode))
        # print(q_network.epsilon)
        if count == 2000:
            q_target_network.network.load_state_dict(q_network.network.state_dict()) # give the weights of the current network to the target network.
            count = 0
torch.save(q_network.network.state_dict(), "dqn_model.pth")
