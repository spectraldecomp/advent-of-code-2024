import numpy as np
from collections import deque

# lines = open('solutions/day12/sample.txt').read().splitlines()
lines = open('solutions/day12/input.txt').read().splitlines()
lines = [list(line) for line in lines]
grid = np.array(lines, dtype=str)
grid = np.pad(grid, pad_width=1, mode='constant', constant_values='&')

def bfs(grid, visited, start, type):
    rows, cols = grid.shape
    queue = deque([start])
    visited.add(start)
    area = 0
    perimeter = 0

    while queue:
        i, j = queue.popleft()
        area += 1
        for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= ni < rows and 0 <= nj < cols:
                if grid[ni, nj] == type:
                    if (ni, nj) not in visited:
                        visited.add((ni, nj))
                        queue.append((ni, nj))
                elif grid[ni, nj] != '&':
                    perimeter += 1 
            else:
                perimeter += 1 
    return area, perimeter

def bfs2(grid, visited, start, type):
    rows, cols = grid.shape
    queue = deque([start])
    visited.add(start)
    area = 0
    sides = 0

    while queue:
        i, j = queue.popleft()
        area += 1
        directions = [(0, 1), (1, 0), (0, -1),(-1, 0)]

        for d in range(4):
            n1_i, n1_j = i + directions[d][0], j + directions[d][1]
            n2_i, n2_j = i + directions[(d + 1) % 4][0], j + directions[(d + 1) % 4][1]

            if 0 <= n1_i < rows and 0 <= n1_j < cols:
                if grid[n1_i, n1_j] == type:
                    if (n1_i, n1_j) not in visited:
                        visited.add((n1_i, n1_j))
                        queue.append((n1_i, n1_j))

            if grid[n1_i, n1_j] != type and grid[n2_i, n2_j] != type:
                sides += 1
            if grid[n1_i, n1_j] == type and grid[n2_i, n2_j] == type:
                n3_i = n1_i + n2_i - i
                n3_j = n1_j + n2_j - j
                if grid[n3_i, n3_j] != type:
                    sides += 1
    return area, sides

rows, cols = grid.shape

visited = set()
price = 0

for i in range(rows):
    for j in range(cols):
        if (i, j) not in visited and grid[i, j] != '&':
            type = grid[i, j]
            area, perimeter = bfs(grid, visited, (i, j), type)
            price += area * perimeter
print("Total Price (Part 1):", price)


visited = set()
price = 0
for i in range(rows):
    for j in range(cols):
        if (i, j) not in visited and grid[i, j] != '&':
            type = grid[i, j]
            area, sides = bfs2(grid, visited, (i, j), type)
            price += area * sides

print("Total Price (Part 2):", price)
