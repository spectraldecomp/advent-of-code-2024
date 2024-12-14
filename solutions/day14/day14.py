import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt


def simulate(robots, width, height, steps):
    positions = []
    for (px, py), (vx, vy) in robots:
        new_x = (px + steps * vx) % width
        new_y = (py + steps * vy) % height
        positions.append((new_x, new_y))
    return positions

def count_quadrants(positions, width, height):
    mid_x, mid_y = width // 2, height // 2
    q1 = q2 = q3 = q4 = 0
    for x, y in positions:
        if x == mid_x or y == mid_y: 
            continue
        if x < mid_x and y < mid_y:
            q1 += 1
        elif x >= mid_x and y < mid_y:
            q2 += 1
        elif x < mid_x and y >= mid_y:
            q3 += 1
        elif x >= mid_x and y >= mid_y:
            q4 += 1
    return q1, q2, q3, q4

#p1

input = open('solutions/day14/input.txt').read()
robots = []
for line in input.strip().split("\n"):
    position, velocity = line.split(" v=")
    px, py = map(int, position[2:].split(","))
    vx, vy = map(int, velocity.split(","))
    robots.append(((px, py), (vx, vy)))

positions = simulate(robots, width=101, height=103, steps=100)
q1, q2, q3, q4 = count_quadrants(positions, width=101, height=103)
print("p1", q1 * q2 * q3 * q4)

def vis(positions, width, height, steps):
    x_coords, y_coords = zip(*positions)
    plt.figure(figsize=(8, 8))
    plt.scatter(x_coords, y_coords, c='blue')
    
    plt.xlim(0, width)
    plt.ylim(0, height)
    plt.title("Robots at step = " + str(steps+1))
    plt.legend()
    plt.grid(True)
    plt.show()
    
    
def simulate2(robots, width, height, steps):
    new_robots = []
    for (px, py), (vx, vy) in robots:
        new_x = (px + steps * vx) % width
        new_y = (py + steps * vy) % height
        new_robots.append(((new_x, new_y), (vx, vy)))
    return new_robots

#p2
min_safety = float('inf')
for i in range(10000):
    robots = simulate2(robots, width=101, height=103, steps=1)
    q1, q2, q3, q4 = count_quadrants([pos for pos, _ in robots], width=101, height=103)
    safety = q1 * q2 * q3 * q4
    if safety < min_safety:
        min_safety = safety
        best_step = i

print("p2", best_step)

print("Done")
    
    


