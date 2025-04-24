import pygame
from player import Player
import player
from maze import Maze
import const
from rl_env import MazeEnv
from agent import QLearningAgent


# Initialize pygame and screen
pygame.init()
global screen # global so it can be accessed everywhere and in different files

# Easier reference to endpoint 
endpoint = [33, 35]

# Player positions initally at top left corner of respective mazes
playerPos = [1, 1] 
NPCPos = [1, 1] 

# Main loop
running = True

# later in charge of ticks
clock = pygame.time.Clock()

#generated mazes to start with
maze1 = Maze.generateMaze(const.MAZE_WIDTH, const.MAZE_HEIGHT)
maze2 = Maze.generateMaze(const.MAZE_WIDTH, const.MAZE_HEIGHT)

# Initially set to false, true when player reaches end
maze1Regen = False
maze2Regen = False

# Set up RL environment and agent
rl_env = MazeEnv()
rl_agent = QLearningAgent(const.MAZE_WIDTH, const.MAZE_HEIGHT)

# Sync agent with inital NPCPos
rl_env.agent_pos = tuple(NPCPos)
rl_env.maze = maze2 # Same maze for NPC and agent

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
        playerPos = [33, 34]

    # Moving player1 with wasd
    if keys[pygame.K_w]:
        Player.movePlayer(playerPos, maze1, 0, -1)
    if keys[pygame.K_s]:
        Player.movePlayer(playerPos, maze1, 0, 1)
    if keys[pygame.K_a]:
        Player.movePlayer(playerPos, maze1, -1, 0)
    if keys[pygame.K_d]:  
        Player.movePlayer(playerPos, maze1, 1, 0)

    if keys[pygame.K_g]:
        print(playerPos)

    # NPC mode
    if keys[pygame.K_UP]:
        Player.movePlayer(NPCPos, maze2, 0, -1)
    if keys[pygame.K_DOWN]:
        Player.movePlayer(NPCPos, maze2, 0, 1)
    if keys[pygame.K_LEFT]:
        Player.movePlayer(NPCPos, maze2, -1, 0)
    if keys[pygame.K_RIGHT]:  
        Player.movePlayer(NPCPos, maze2, 1, 0)
    
    # generating a new maze when player reaches endpoint
    if playerPos == endpoint:
        maze1Regen = True
    if NPCPos == endpoint:
        maze2Regen = True

    if maze1Regen:
        maze1 = Maze.generateMaze(const.MAZE_WIDTH, const.MAZE_HEIGHT)
        maze1Regen = False
    if maze2Regen:
        maze2 = Maze.generateMaze(const.MAZE_WIDTH, const.MAZE_HEIGHT)
        maze2Regen = False

    # Render mazes
    Maze.renderMaze(maze1, Maze.screen, 0, const.DARK_RED, const.MED_SIZE)
    Maze.renderMaze(maze2, Maze.screen, (const.MAZE_WIDTH * const.MED_SIZE), const.DARK_CYAN, const.MED_SIZE)

    #Render player and NPC
    play = Player(playerPos[0], playerPos[1])
    play.draw(Maze.screen, const.MED_SIZE, 0, const.RED)

    npc_agent = Player(NPCPos[0], NPCPos[1])
    npc_agent.draw(Maze.screen, const.MED_SIZE, (const.MAZE_WIDTH + const.MED_SIZE), const.CYAN)

    # RL Agent movement
    rl_env.agent_pos = tuple(NPCPos)
    rl_env.maze = maze2
    state = rl_env._get_state()
    action = rl_agent.choose_action(state)
    _, _, _, _ = rl_env.step(action)
    NPCPos = list(rl_env.agent_pos) # Update visual NPC position

    # Calling score to award points
    Player.score(maze1, False, playerPos)
    Player.score(maze2, True, NPCPos)

    # Displaying it on screen
    Player.drawScore(Maze.screen, player.pScore, player.NPCScore)
    if(player.pScore == 5):
        Maze.screen.fill((0, 0, 0))
        Player.drawWin(Maze.screen,True, False)
    elif(player.NPCScore == 5):
        Maze.screen.fill((0, 0, 0))
        Player.drawWin(Maze.screen, False, True)
        while(True):
            NPCpos = [1, 1]
    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(10) 

pygame.quit()
