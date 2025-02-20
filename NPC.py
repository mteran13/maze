import pygame

CELL_SIZE = 18
WIDTH = 1188 # total width of screen
HEIGHT = 486 # total height
MAZE_WIDTH = WIDTH // 2  // CELL_SIZE 
MAZE_HEIGHT = HEIGHT // CELL_SIZE

class NPC:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 255), (self.x * CELL_SIZE + MAZE_WIDTH * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def aiMove(self, maze, dx, dy):
        if 0 <= self.x + dx < len(maze[0]) and 0 <= self.y + dy < len(maze):
            if abs(dx) > abs(dy):
                self.x += 1 if dx > 0 else -1
            else:
                self.y += 1 if dy > 0 else -1