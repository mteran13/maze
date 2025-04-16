# all constants
import pygame

MED_SIZE = 18 # default size
"""
HARD_SIZE = 6
EASY_SIZE = 24"
implement later if I do difficulty
"""

WIDTH = 1300 # total width of screen
HEIGHT = 700 # total height
MAZE_WIDTH = WIDTH // 2  // MED_SIZE 
MAZE_HEIGHT = HEIGHT // MED_SIZE

pygame.font.init()
FONT = pygame.font.Font("/home/mteran/.local/share/fonts/PressStart2P.ttf", 15)

"""text_surface = FONT.render("Player: ", True, (255, 255, 255))
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.blit(text_surface, (0, 0))
    pygame.display.update()

"""
# Colors so I don't have to do slightly more work
BLACK = (0, 0, 0) 
RED = (255, 0, 0)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)
DARK_RED = (70, 0, 0)
DARK_CYAN = (0, 70, 70)
