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

RED = (255, 0, 0)
CYAN = (0, 255, 255)
DARK_RED = (60, 40, 40)
DARK_CYAN = (40, 60, 60)

pScore = 0
NPCScore = 0

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


    def score(maze, isMaze2, player):
        global pScore
        global NPCScore

        if player[1] == 25 and player[0] == 31:
            player[0], player[1] = 1, 1
            if (isMaze2):
                offset = MAZE_WIDTH * MED_SIZE
                color = DARK_CYAN
                NPCScore += 1
            else:
                offset = 0
                color = DARK_RED
                pScore += 1
            nu = Maze.generateMaze(MAZE_WIDTH, MAZE_HEIGHT)
            Maze.renderMaze(nu, Maze.screen, offset, color, MED_SIZE)
            return ("player: " + str(pScore) + "NPC: " + str(NPCScore))
    
    def drawScore(screen, pScore, NPCScore):
        pygame.font.init()
        font = pygame.font.SysFont('ubuntu sans', 15)
    
        pScoreText = font.render(f"Player: {pScore}", True, RED)
        NPCScoreText = font.render(f"NPC: {NPCScore}", True, CYAN)

        screen.blit(pScoreText, (0, 0))
        screen.blit(NPCScoreText, (WIDTH / 2, 0))
