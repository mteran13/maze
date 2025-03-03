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

# def aiMove not implemented (but soon)
