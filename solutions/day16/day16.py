from collections import deque
import numpy as np

def maze(maze):
    maze = maze.strip().split("\n")
    rows, cols = len(maze), len(maze[0])

    # parse maze to find start and end
    start = end = None
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    dp = np.full((rows, cols, 4), float('inf'))
    for d in range(4):
        dp[start[0]][start[1]][d] = 0

    # BFS
    queue = deque([(start[0], start[1], d) for d in range(4)]) 
    while queue:
        x, y, d = queue.popleft()
        current_cost = dp[x][y][d]
        
        # Move forward
        dx, dy = directions[d]
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != '#':
            # If the cost to reach (nx, ny) from (x, y) is less than the current cost, 
            # update the cost and add to the queue
            if current_cost + 1 < dp[nx][ny][d]:
                dp[nx][ny][d] = current_cost + 1
                queue.append((nx, ny, d))

        # Rotate
        for turn_cost, new_d in [(1000, (d - 1) % 4), (1000, (d + 1) % 4)]:
            # If the cost to rotate is less than the current cost, 
            # update the cost and add to the queue
            if current_cost + turn_cost < dp[x][y][new_d]:
                dp[x][y][new_d] = current_cost + turn_cost
                queue.append((x, y, new_d))
    
    # Find minimum cost to reach the end
    min_cost = min(dp[end[0]][end[1]])
    
    # Find all paths with minimum cost
    all_paths = []
    queue = deque()
    
    # Get all directions with minimum cost from the end
    for d in range(4):
        if dp[end[0]][end[1]][d] == min_cost:
            queue.append((end[0], end[1], d, []))
            
    while queue:
        # BFS to find all paths with minimum cost
        x,y,d,path = queue.popleft()
        path.append((x,y))
        # If we reach the start, add the path to all_paths
        if (x,y) == start:
            all_paths.append(path[::-1])
            continue
        for dir_idx, (dx, dy) in enumerate(directions):
            nx, ny = x - dx, y - dy
            # Move forward
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != '#':
                # If the cost to reach (nx, ny) from (x, y) is less than the current cost,
                # add to the queue
                if dp[nx][ny][dir_idx] + 1 == dp[x][y][d]:
                    queue.append((nx, ny, dir_idx, path.copy()))
                # Rotation
                # If the cost to rotate is less than the current cost,
                # add to the queue
                if dp[x][y][dir_idx] + 1000 == dp[x][y][d]:
                    queue.append((nx, ny, dir_idx, path.copy()))
    best_path_tiles = set()
    # Find the tiles in the best path
    for path in all_paths:
        best_path_tiles.update(path)
    return len(best_path_tiles)
    
    
# Example usage
input_data = open("solutions/day16/sample.txt").read()
input_data = open("solutions/day16/input.txt").read()

print(maze(input_data))
