import numpy as np 
import torch
import torch.nn as nn
import torch.optim as optim

class Q_learningAgent:
    def __init__(self):

        self.q_table = np.zeros((4,4,4))
        self.alpha = 0.5
        self.gamma = 0.8
        self.epsilon = 1

    def choose_action(self,state):
        x = np.random.choice([0, 1], p=[self.epsilon, 1-self.epsilon])
        if x ==0:
        # first option (random action)
            action = np.random.randint(0,4)
        else:
        # second option (best q-value for that state)
            q_values_all_actions = self.q_table[[state[0]],[state[1]]]
            action = np.argmax(q_values_all_actions)
        return action

    def update_q_values(self,state,reward,next_state,action):
        current_q = self.q_table[state[0],state[1],action]
        best_next_q = np.max(self.q_table[next_state[0],next_state[1]])
        # q-learning equation
        self.q_table[state[0],state[1],action]=current_q+self.alpha*(reward+self.gamma*best_next_q-current_q)
        # return self.q_table

class Deep_Q_learningAgent(nn.Module):
    def __init__(self):
        super().__init__()
        self.gamma = 0.99
        self.epsilon = 1
        self.learning_rate = 0.001

        self.network = nn.Sequential(
            nn.Linear(64, 64),   # Input: map with the state encoded
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 4)     # Output: the four possible actions: up, down, left, right

        )
        self.optimizer = optim.Adam(self.network.parameters(),lr=self.learning_rate)
        self.criterion = nn.MSELoss()
        
    def forward(self,x):
        return self.network(x)
    
    def choose_action(self,env):
        x = np.random.choice([0, 1], p=[self.epsilon, 1-self.epsilon])
        if x ==0:
        # first option (random action)
            action = np.random.randint(0,4)
        # second option (take the highest q value of the neural network)
        else:
            encoded_map = self.encoding_input(env)
            q_value_actions = self.forward(encoded_map)
            action = np.argmax(q_value_actions)
        return action
        

    def train_step(self, state, action, reward, next_state, done):
        pass

    def encoding_input(self,env):
        self.encoded_input = []
        for row in range(len(env.grid)):
            for col in range(len(env.grid[0])):
                if env.grid[row][col]=='P':
                    self.encoded_input.append([1,0,0,0])
                elif env.grid[row][col]==' ':
                    self.encoded_input.append([0,1,0,0])
                elif env.grid[row][col]=='H':
                    self.encoded_input.append([0,0,1,0]) 
                else: 
                    self.encoded_input.append([0,0,0,1])
        self.encoded_input = torch.tensor(self.encoded_input,dtype=torch.float32).flatten()
        print(self.encoded_input)
        return self.encoded_input

