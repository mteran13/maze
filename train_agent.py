from rl_env import MazeEnv
from agent import QLearningAgent
from const import MAZE_HEIGHT, MAZE_WIDTH

env = MazeEnv()
agent = QLearningAgent(MAZE_HEIGHT, MAZE_WIDTH)

episodes = 1000

for episode in range(episodes):
    state = env.reset()
    done = False
    total_reward = 0

    while not done:
        action = agent.choose_action(state)
        next_state, reward, done, _ = env.step(action)
        agent.learn(state, action, reward, next_state)
        state = next_state
        total_reward += reward 

    if episode % 100 == 0:
        print(f"Episode {episode}, total reward: {total_reward}")
