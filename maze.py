import random
import pygame
import time


MED_SIZE = 18 # default size
"""
HARD_SIZE = 6
EASY_SIZE = 24"
implement later if I do difficulty
"""

WIDTH = 1188 # total width of screen
HEIGHT = 486 # total height
MAZE_WIDTH = WIDTH // 2  // MED_SIZE 
MAZE_HEIGHT = HEIGHT // MED_SIZE 

# Colors so I don't have to do slightly more work
BLACK = (0, 0, 0) 
RED = (255, 0, 0)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)
DARK_RED = (60, 40, 40)
DARK_CYAN = (40, 60, 60)

class Maze:
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Lot of help from geeksforgeeks.org and stack overflow to get syntax for backtracking algorithm
    def generateMaze(width, height):
        random.seed(time.time()) # use current time as seed for random num
        maze = [[1 for _ in range(width)] for _ in range(height)] # Generate matrix of 1s 

        def carve(x, y):
            maze[y][x] = '' # Carve out the space

            directions = [(0,1), (1,0), (0, -1), (-1, 0)]
            random.shuffle(directions) # Decides random direction to go

            for dx, dy in directions:
                nx, ny = x + dx * 2, y + dy * 2
                if 0 < nx < width - 1 and 0 < ny < height - 1 and maze[ny][nx] == 1: # Checking bounds 
                    maze[ny][nx] = ''
                    maze[y + dy][x + dx] = '' # Carve wall between cells
                    carve(nx, ny)
        carve(1, 1) # Goes through function starting at 1,1
        return maze
    
    def renderMaze(maze, screen, offset, accent, size):
        for y in range(MAZE_HEIGHT):
            for x in range(MAZE_WIDTH):
                color = BLACK if maze[y][x] == 1 else accent
                # Differs from maze 2 by adding maze width * cell size
                pygame.draw.rect(screen, color, (x * size + offset, y * size, size, size))
        pygame.draw.rect(screen, GREEN, (31 * size + offset, 25 * size, size, size))
