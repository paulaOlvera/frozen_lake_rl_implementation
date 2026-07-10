import numpy as np
from agents import Q_learningAgent, Deep_Q_learningAgent
from gridworld import GridWorld

env = GridWorld(True)
deep_agent = Deep_Q_learningAgent()
print(np.size(deep_agent.encoding_input(env)))
print(deep_agent)
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