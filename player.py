import pygame
from maze import Maze

CELL_SIZE = 18
WIDTH = 1188 # total width of screen
HEIGHT = 486 # total height
MAZE_WIDTH = WIDTH // 2  // CELL_SIZE 
MAZE_HEIGHT = HEIGHT // CELL_SIZE

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    # Player movement
    def movePlayer(playerPos, maze, dx, dy):
        x, y = playerPos # player_pos is a list, index 0 = x, index 1 = y

        if 0 <= x + dx < len(maze[0]) and 0 <= y + dy < len(maze):
            if maze[y + dy][x + dx] == '': 
                playerPos[0] += dx
                playerPos[1] += dy

    # does not work lmao  
    def score(playerPos, endPoint, score):
        while playerPos[0] == endPoint[0] and playerPos[1] == endPoint[1]:
            score = score + 1
            break
            
