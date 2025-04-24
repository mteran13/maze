import numpy as np
from maze import Maze
import pygame
from const import MED_SIZE, MAZE_HEIGHT, MAZE_WIDTH
# not the correct names for constants

class MazeEnv:
    def __init__(self):
        self.maze = Maze()
        self.goal = (33, 35)
        self.reset

    def reset(self):
        # reset maze and cyan player
        self.maze.generate_maze()
        self.agent_pos = self.maze.start
        self.goal = self.maze.end
        return self._get_state()
    
    def _get_state(self):
        return self.agent_pos
    
    def step(self, action):
        # Move cyan player based on action
        # Compute reward, check if done
        x, y = self.agent_pos
        dx, dy = [(0, -1), (0, 1), (-1, 0), (1, 0)][action]
        new_pos = (x + dx, y + dy)

        # Check if within bounds and not a wall
        if (0 <= new_pos[0] < MAZE_WIDTH) and (0 <= new_pos[1] < MAZE_HEIGHT) and self.maze[new_pos[1]][new_pos[0]] == '':
            self.agent_pos = new_pos
        reward = -0.01 # Time penalty
        done = False

        if self.agent_pos == self.goal:
            reward = 1.0
            done = True

        return self._get_state(), reward, done, {}
    
    def render(self, screen):
        #Optional use pygame to draw maze and players
        x, y = self.agent_pos
        rect = pygame.Rect(x * MED_SIZE, y * MED_SIZE, MED_SIZE, MED_SIZE)
        pygame.draw.rect(screen, (0, 255, 255), rect)
