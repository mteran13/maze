"""
NEED
environment
agent
state
action
reward
"""

import random
import numpy as np

class Agent:
    def __init__(self, maze):
        self.x, self.y = 1, 1
        self.maze = maze
        self.directions = ["up", "down", "left", "right"]
        self.q_table = np.zeros((maze.height, maze.width, len(self.directions)))
        self.learning_rate = 0.1
        self.discount_factor = 0.9
        self.exploration_rate = 1.0 # Starting with full
        self.exploration_decay = 0.995
        self.min_exploration_rate = 0.1
        self.reward = -1 # Penalty to encourage exploration

    def chooseAction(self):
        if random.uniform(0, 1) < self.exploration_rate:
            return random.choice(self.directions) # Explore
        else:
            action_index = np.argmax(self.q_table[self.y, self.x]) # Exploit
            return self.directions[action_index]
        
    def move(self, action):
        dx, dy = action
        newX, newY = self.x + dx, self.y + dy

        if self.maze.isValidMove(newX, newY):
            self.x, self.y = newX, newY
    
    def updateQTable(self, prevX, prevY, action, reward, nextX, nextY):
        prevQValue = self.q_table[prevY, prevX, self.directions.index(action)]
        futureQValue = np.max(self.q_table[nextY, nextX])
        # Q Learning formula
        self.q_table[prevY, prevX, self.directions.index(action)] = prevQValue + self.learning_rate * (reward + self.discount_factor * futureQValue - prevQValue)

    def decayExplorationRate(self):
        if self.exploration_rate > self.min_exploration_rate:
            self.exploration_rate *= self.exploration_decay
            
            

        