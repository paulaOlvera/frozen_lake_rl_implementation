import numpy as np 

class Agent:
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
