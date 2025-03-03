import pygame
from maze import Maze
from NPC import NPC

HARD_SIZE = 6
MED_SIZE = 18 # default size
EASY_SIZE = 24

WIDTH = 1188 # total width of screen
HEIGHT = 486 # total height
MAZE_WIDTH = WIDTH // 2  // MED_SIZE 
MAZE_HEIGHT = HEIGHT // MED_SIZE

DARK_RED = (60, 40, 40)
DARK_CYAN = (40, 60, 60)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self, screen, size):
        pygame.draw.rect(screen, (255, 0, 0), (self.x * size, self.y * size, size, size))
    
    # Player movement
    def movePlayer(playerPos, maze, dx, dy):
        x, y = playerPos # player_pos is a list, index 0 = x, index 1 = y

        if 0 <= x + dx < len(maze[0]) and 0 <= y + dy < len(maze):
            if maze[y + dy][x + dx] == '': 
                playerPos[0] += dx
                playerPos[1] += dy

    # Currently broken - not recognizing when players reach endpoint
    def score(maze, isMaze2, player, score):
        if player[1] == 25 and player[0] == 31:
            score = score + 1
            player[0], player[1] = 1, 1
            if (isMaze2):
                offset = MAZE_WIDTH * MED_SIZE
                color = DARK_CYAN
                player = NPC(1, 1)
            else:
                player = Player(1, 1)
                offset = 0
                color = DARK_RED 
            new = Maze.generateMaze(MAZE_WIDTH, MAZE_HEIGHT)
            Maze.renderMaze(new, Maze.screen, offset, color, MED_SIZE)   
              

