import pygame
from player import Player
from maze import Maze
from NPC import NPC

# Constants
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

# Initialize pygame and screen
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Generate two mazes
maze1 = Maze.generateMaze(MAZE_WIDTH, MAZE_HEIGHT)
maze2 = Maze.generateMaze(MAZE_WIDTH, MAZE_HEIGHT)
endpoint = [31, 25]

# Player positions
player1Pos = [1, 1] # Top left corner of maze 1
NPCPos = [1, 1] # Top left corner of maze 2
p1Score = 0
p2Score = 0

# Main loop
running = True
clock = pygame.time.Clock()

while running:

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
        player1Pos = [1,1]
    if keys[pygame.K_RSHIFT]:
        NPCPos = [1,1]

    # Moving player1 with wasd
    if keys[pygame.K_w]:
        Player.movePlayer(player1Pos, maze1, 0, -1)
        Player.score(player1Pos, endpoint, p1Score)
    if keys[pygame.K_s]:
        Player.movePlayer(player1Pos, maze1, 0, 1)
        Player.score(player1Pos, endpoint, p1Score)
    if keys[pygame.K_a]:
        Player.movePlayer(player1Pos, maze1, -1, 0)
        Player.score(player1Pos, endpoint, p1Score)
    if keys[pygame.K_d]:  
        Player.movePlayer(player1Pos, maze1, 1, 0)
        Player.score(player1Pos, endpoint, p1Score)
    
    # Moving NPC with arrow keys
    dx, dy = 0, 0
    if keys[pygame.K_UP]:
        Player.movePlayer(NPCPos, maze2, 0, -1)
        Player.score(NPCPos, endpoint, p2Score)
    if keys[pygame.K_DOWN]:
        Player.movePlayer(NPCPos, maze2, 0, 1)
        Player.score(NPCPos, endpoint, p2Score)
    if keys[pygame.K_LEFT]:
        Player.movePlayer(NPCPos, maze2, -1, 0)
        Player.score(NPCPos, endpoint, p2Score)
    if keys[pygame.K_RIGHT]:
        Player.movePlayer(NPCPos, maze2, 1, 0)
        Player.score(NPCPos, endpoint, p2Score)
   
    # Render mazes
    Maze.renderMaze(maze1, screen, 0, DARK_RED)
    Maze.renderMaze(maze2, screen, (MAZE_WIDTH * CELL_SIZE), DARK_CYAN)
    
    # Render player & NPC
    player = Player(player1Pos[0], player1Pos[1])
    player.draw(screen)

    npc = NPC(NPCPos[0], NPCPos[1])
    npc.draw(screen)

    # Text for scores
    pygame.font.init()
    font = pygame.font.SysFont('ubuntu sans', 15)
    
    text1 = font.render('Player 1: ' + str(p1Score), True, (RED))
    text2 = font.render('Player 2: ' + str(p2Score), True, (CYAN))

    screen.blit(text1, (0, 0))
    screen.blit(text2, (WIDTH / 2, 0))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(13) # lucky number :)
pygame.quit()