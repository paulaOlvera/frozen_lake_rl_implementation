from agents import Deep_Q_learningAgent
from gridworld import GridWorld
import torch 
deep_network= Deep_Q_learningAgent()
env = GridWorld(True)
deep_network.network.load_state_dict(torch.load("dqn_model.pth"))

if __name__ == '__main__': 
    print("**************Game starts **************************")
    done = False
    env.reset()

    while not done:
        
        deep_network.epsilon = 0
        action = deep_network.choose_action(env)
        next_state, reward, done = env.step(action)
        print()
        env.render()
        if done:
            print("**************Game over **************************")
