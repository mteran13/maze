import numpy as np
import random

class QLearningAgent:
    def __init__(self, rows, cols, n_actions = 4, alpha = 0.1, gamma = 0.9, epsilon = 0.1):
        self.q_table = np.zeros((rows, cols, n_actions))
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor
        self.epsilon = epsilon  # Exploration rate
        self.n_actions = n_actions

    def choose_action(self, state):
        x, y = state
        if random.random() < self.epsilon:
            return random.randint(0, self.n_actions - 1)
        else:
            return np.argmax(self.q_table[y, x]) # y row, x column
        
    def learn(self, state, action, reward, next_state):
        x, y = state
        nx, ny = next_state
        predict = self.q_table[y, x, action]
        target = reward + self.gamma * np.max(self.q_table[ny, nx])
        self.q_table[y, x, action] += self.alpha * (target - predict)