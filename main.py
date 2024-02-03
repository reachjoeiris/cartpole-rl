'''
# steps:
    1. install miniconda
    2. create env
    3. conda install python=3.11
    4. pip install gymnasium[classic-control]
'''
    
 
# classical gym 
import gymnasium as gym
import numpy as np
import time
 
 
# create cartpole environment
env=gym.make('CartPole-v1',render_mode='human')

# simulate the environment
episodeNumber=5
timeSteps=100
 
for episodeIndex in range(episodeNumber):
    initial_state=env.reset()
    print(episodeIndex)
    env.render()
    appendedObservations=[]
    for timeIndex in range(timeSteps):
        print(timeIndex)
        random_action=env.action_space.sample()
        observation, reward, terminated, truncated, info =env.step(random_action)
        appendedObservations.append(observation)
        time.sleep(0.1)
        if (terminated):
            time.sleep(1)
            break
env.close()  