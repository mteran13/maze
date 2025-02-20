import random
import pygame

CELL_SIZE = 18
WIDTH = 1188 # total width of screen
HEIGHT = 486 # total height
MAZE_WIDTH = WIDTH // 2  // CELL_SIZE 
MAZE_HEIGHT = HEIGHT // CELL_SIZE

# Colors so I don't have to do slightly more work
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)
DARK_RED = (60, 40, 40)
DARK_CYAN = (40, 60, 60)

class Maze:

    # Lot of help from geeksforgeeks.org and stack overflow to get syntax for backtracking algorithm
    def generateMaze(width, height):
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
    
    def renderMaze(maze, screen, offset, accent):
        for y in range(MAZE_HEIGHT):
            for x in range(MAZE_WIDTH):
                color = BLACK if maze[y][x] == 1 else accent
                # Differs from maze 2 by adding maze width * cell size
                pygame.draw.rect(screen, color, (x * CELL_SIZE + offset, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            # endpoint: 31,25
        pygame.draw.rect(screen, GREEN, (31 * CELL_SIZE + offset, 25 * CELL_SIZE, CELL_SIZE, CELL_SIZE))
