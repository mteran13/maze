import pygame
from collections import deque

MED_SIZE = 18 # default size
"""
HARD_SIZE = 6
EASY_SIZE = 24
implement later if I do difficulty
"""

WIDTH = 1188 # total width of screen
HEIGHT = 486 # total height
MAZE_WIDTH = WIDTH // 2  // MED_SIZE 
MAZE_HEIGHT = HEIGHT // MED_SIZE

RED = (255, 0, 0)
CYAN = (0, 255, 255)
DARK_RED = (70, 0, 0)
DARK_CYAN = (0, 70, 70)

pScore = 0
NPCScore = 0

directions = ["up", "down", "left", "right"]

class Player:
    #Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # draws player
    def draw(self, screen, size, offset, color):
        pygame.draw.rect(screen, color, (self.x * size + offset, self.y * size, size, size))
    
    # Player movement
    def movePlayer(playerPos, maze, dx, dy):
        x, y = playerPos # player_pos is a list, index 0 = x, index 1 = y

        if 0 <= x + dx < len(maze[0]) and 0 <= y + dy < len(maze):
            if maze[y + dy][x + dx] == '': 
                playerPos[0] += dx
                playerPos[1] += dy

    # adds to respective scores if player reaches end
    def score(maze, isMaze2, player):
        global pScore
        global NPCScore
        
        if player[1] == 25 and player[0] == 31:
            if (isMaze2):
                NPCScore += 1
                player[0], player[1] = 1, 1
            else:
                pScore += 1
                player[0], player[1] = 1, 1

    # draws the score on screen at top    
    def drawScore(screen, pScore, NPCScore):
        pygame.font.init()
        font = pygame.font.SysFont('ubuntu sans', 15)
    
        pScoreText = font.render(f"Player: " + str(pScore), True, RED)
        NPCScoreText = font.render(f"(future) NPC: " + str(NPCScore), True, CYAN)

        screen.blit(pScoreText, (0, 0))
        screen.blit(NPCScoreText, (WIDTH / 2, 0))

class NPC(Player):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.path = []
    
    # supposed pathfinding - does not work right now
    def findPath(self, maze, start, goal):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up
        # BFS to find shortest path
        queue = deque([(start[0], start[1], [])])
        visited = set()
        visited.add((start[0], start[1]))

        while queue:
            x, y, path = queue.popleft()
            # If reached goal, return path
            if (x, y) == goal:
                return path
            # Check all 4 directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and maze[ny][nx] == '' and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, path + [(nx, ny)]))
        return []
    
    def moveNPC(self, maze, goal):
        # Find next step in path to goal
        self.path = self.findPath(maze, [self.x, self.y], goal)

        if self.path:
            nextStep = self.path[0] #Take first step to goal
            self.x, self.y = nextStep

    
