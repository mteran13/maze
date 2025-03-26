import pygame
from player import Player
import player
from maze import Maze

# Constants
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

# Initialize pygame and screen
pygame.init()
global screen

# Generate two mazes
maze1 = Maze.generateMaze(MAZE_WIDTH, MAZE_HEIGHT)
maze2 = Maze.generateMaze(MAZE_WIDTH, MAZE_HEIGHT)
endpoint = [31, 25]

# Player positions
playerPos = [1, 1] # Top left corner of maze 1
NPCPos = [1, 1] # Top left corner of maze 2

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    Maze.screen.fill((0, 0, 0))

     # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys for player movement
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_ESCAPE]:
        running = False

    # Resets player positions to start if they want
    if keys[pygame.K_LSHIFT]:
        playerPos = [1,1]
    if keys[pygame.K_RSHIFT]:
        NPCPos = [1,1]

    # For dev, take this out later
    if keys[pygame.K_f]:
        playerPos = [31, 24]

    # Moving player1 with wasd
    if keys[pygame.K_w]:
        Player.movePlayer(playerPos, maze1, 0, -1)
    if keys[pygame.K_s]:
        Player.movePlayer(playerPos, maze1, 0, 1)
    if keys[pygame.K_a]:
        Player.movePlayer(playerPos, maze1, -1, 0)
    if keys[pygame.K_d]:  
        Player.movePlayer(playerPos, maze1, 1, 0)
    
    # Moving NPC with arrow keys
    dx, dy = 0, 0
    if keys[pygame.K_UP]:
        Player.movePlayer(NPCPos, maze2, 0, -1)    
    if keys[pygame.K_DOWN]:
        Player.movePlayer(NPCPos, maze2, 0, 1)
    if keys[pygame.K_LEFT]:
        Player.movePlayer(NPCPos, maze2, -1, 0)
    if keys[pygame.K_RIGHT]:
        Player.movePlayer(NPCPos, maze2, 1, 0)
       

    size = MED_SIZE
    """
    I implement this later for an optional step ok ok
    if size == 1:
        size = EASY_SIZE
    elif size == 3:
        size = HARD_SIZE
    """

    # Render mazes
    Maze.renderMaze(maze1, Maze.screen, 0, DARK_RED, size)
    Maze.renderMaze(maze2, Maze.screen, (MAZE_WIDTH * MED_SIZE), DARK_CYAN, size)
    
    # Render player & NPC
    play = Player(playerPos[0], playerPos[1])
    play.draw(Maze.screen, size, 0, RED)

    npc = player.NPC(NPCPos[0], NPCPos[1])
    npc.draw(Maze.screen, size, (MAZE_WIDTH * MED_SIZE), CYAN)
    npc.aiMove()
    
    Player.score(maze1, False, playerPos)
    Player.score(maze2, True, NPCPos)

    Player.drawScore(Maze.screen, player.pScore, player.NPCScore)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(13) # lucky number :)

pygame.quit()
