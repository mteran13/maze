from maze import Maze
import pygame
import heapq
from const import MED_SIZE, MAZE_HEIGHT, MAZE_WIDTH

class Test:
    def heuristic(pos, goal):
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])
    
    def reconstruct_path(came_from, current):
        path = []
        while current in came_from:
            path.append(current)
            current = came_from[current]
        path.reverse()
        return path

    # Testing A* pathfinding algorithm
    def a_star(maze, start, goal):
        open_list = []
        closed_list = set()
        

        #Cost frpm start tp current position
        g_cost = {start : 0}

        # Estimated cost from current position
        f_cost = {start : Test.heuristic(start, goal)}

        # Parent nodes to reconstruct path
        came_from = {}

        heapq.heappush(open_list, (f_cost[start], start))

        while open_list:
            _, current = heapq.heappop(open_list)

            if current == goal:
                return Test.reconstruct_path(came_from, current)
            
            closed_list.add(current)

            for dx, dy in [(0,-1), (0, 1), (-1, 0), (1, 0)]:
                neighbor = (current[0] + dx, current[1] + dy)
                if 0 <= neighbor[0] < len(maze[0]) and 0 <= neighbor[1] < len(maze):
                    if maze[neighbor[1]][neighbor[0]] != '' or neighbor in closed_list:
                        continue

                    tentative_g_cost = g_cost[current] + 1
                    if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                        came_from[neighbor] = current
                        g_cost[neighbor] = tentative_g_cost
                        f_cost[neighbor] = g_cost[neighbor] + Test.heuristic(neighbor, goal)
                        heapq.heappush(open_list, (f_cost[neighbor], neighbor))
        return []
    
    
    
    #Use A* for pathfinding in step function
    def step(self, action):
        x, y = self.agent_pos
        dx, dy = [(0, -1), (0, 1), (-1, 0), (1, 0)][action]
        new_pos = (x + dx, y + dy)

        # Check if move is valid
        if (0 <= new_pos[0] < MAZE_WIDTH) and (0 <= new_pos[1] < MAZE_HEIGHT) and self.maze[new_pos[1]][new_pos[0]] == '':
            self.agent_pos = new_pos

        reward = -0.01
        done = False
        if self.agent_pos == self.goal:
            reward = 1.0
            done = True
        
        return self._get_state(), reward, done, {}
