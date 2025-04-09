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
DARK_RED = (70, 0, 0)
DARK_CYAN = (0, 70, 70)

# Initialize pygame and screen
pygame.init()
global screen # global so it can be accessed everywhere and in different files

# Easier reference to endpoint 
endpoint = [31, 25]

# Player positions initally at top left corner of respective mazes
playerPos = [1, 1] 
NPCPos = [1, 1] 

# Main loop
running = True

# later in charge of ticks
clock = pygame.time.Clock()

#generated mazes to start with
maze1 = Maze.generateMaze(MAZE_WIDTH, MAZE_HEIGHT)
maze2 = Maze.generateMaze(MAZE_WIDTH, MAZE_HEIGHT)

# Initially set to false, true when player reaches end
maze1Regen = False
maze2Regen = False

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

    # For test purposes (gets to end faster)
    if keys[pygame.K_UP]:
        NPCPos = [31, 24]
    if keys[pygame.K_DOWN]:
        Player.movePlayer(NPCPos, maze2, 0, 1)
    
    # in charge of generating a new maze when player reaches endpoint
    if playerPos == endpoint:
        maze1Regen = True
    if NPCPos == endpoint:
        maze2Regen = True

    if maze1Regen:
        maze1 = Maze.generateMaze(MAZE_WIDTH, MAZE_HEIGHT)
        maze1Regen = False
    if maze2Regen:
        maze2 = Maze.generateMaze(MAZE_WIDTH, MAZE_HEIGHT)
        maze2Regen = False

    # Render mazes
    Maze.renderMaze(maze1, Maze.screen, 0, DARK_RED, MED_SIZE)
    Maze.renderMaze(maze2, Maze.screen, (MAZE_WIDTH * MED_SIZE), DARK_CYAN, MED_SIZE)

    #Render player and NPC
    play = Player(playerPos[0], playerPos[1])
    play.draw(Maze.screen, MED_SIZE, 0, RED)

    npc = player.NPC(NPCPos[0], NPCPos[1])
    npc.draw(Maze.screen, MED_SIZE, (MAZE_WIDTH * MED_SIZE), CYAN)

    # Calling score to award points
    Player.score(maze1, False, playerPos)
    Player.score(maze2, True, NPCPos)

    # Displaying it on screen
    Player.drawScore(Maze.screen, player.pScore, player.NPCScore)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(10) 

pygame.quit()
