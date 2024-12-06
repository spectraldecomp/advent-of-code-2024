import numpy as np


# lines = open('solutions/day06/sample.txt').read().splitlines()
lines = open('solutions/day06/input.txt').read().splitlines()
slines = [list(line) for line in lines]
x = np.array(slines)
x = np.pad(x, 1, mode='constant', constant_values='A')


start_char = '^'
visited_cells = set()

def in_grid(coords):
    return x[coords[0], coords[1]] != 'A'


# p1
coords = [np.where(x == start_char)[0][0], np.where(x == start_char)[1][0]]
visited_cells.add(tuple(coords))
direction = 'up'
while in_grid(coords):
    if direction == 'up':
        if x[coords[0] - 1, coords[1]] != '#':
            coords[0] -= 1
        else:
            direction = 'right'
    elif direction == 'right':
        if x[coords[0], coords[1] + 1] != '#':
            coords[1] += 1
        else:
            direction = 'down'
    elif direction == 'down':
        if x[coords[0] + 1, coords[1]] != '#':
            coords[0] += 1
        else:
            direction = 'left'
    elif direction == 'left':
        if x[coords[0], coords[1] - 1] != '#':
            coords[1] -= 1
        else:
            direction = 'up'
    if in_grid(coords):
        visited_cells.add(tuple(coords))

print(len(visited_cells))

# p2
loop_ct = 0
for cell in visited_cells:
    coords = [np.where(x == start_char)[0][0], np.where(x == start_char)[1][0]]
    visited_cells_new = set()
    x_copy = np.copy(x)
    x_copy[cell[0], cell[1]] = '#'
    
    direction = 'up'
    while in_grid(coords):
        if direction == 'up':
            if x_copy[coords[0] - 1, coords[1]] != '#':
                coords[0] -= 1
            else:
                direction = 'right'
        elif direction == 'right':
            if x_copy[coords[0], coords[1] + 1] != '#':
                coords[1] += 1
            else:
                direction = 'down'
        elif direction == 'down':
            if x_copy[coords[0] + 1, coords[1]] != '#':
                coords[0] += 1
            else:
                direction = 'left'
        elif direction == 'left':
            if x_copy[coords[0], coords[1] - 1] != '#':
                coords[1] -= 1
            else:
                direction = 'up'
        if in_grid(coords):
            if (tuple(coords), direction) in visited_cells_new:
                loop_ct += 1
                break
            visited_cells_new.add((tuple(coords), direction))

print(loop_ct)