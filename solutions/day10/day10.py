import numpy as np
import itertools
lines = open('solutions/day10/sample.txt').read().splitlines()
# lines = open('solutions/day10/input.txt').read().splitlines()

x = np.array([list(map(int, line)) for line in lines])
lenx,leny = x.shape


table1 = [[set() for _ in range(leny)] for _ in range(lenx)]
table2 = np.zeros((lenx, leny), dtype=int)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#p1 
for i in range(lenx):
    for j in range(leny):
        if x[i, j] == 9:
            table1[i][j].add((i, j))
for value in range(8, -1, -1):
    for i in range(lenx):
        for j in range(leny):
            if x[i, j] == value:
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < lenx and 0 <= nj < leny and x[ni, nj] == value + 1:
                        table1[i][j].update(table1[ni][nj])
score = 0
for i in range(lenx):
    for j in range(leny):
        if x[i, j] == 0:
            score += len(table1[i][j])
print(score)

#p2
for i in range(lenx):
    for j in range(leny):
        if x[i, j] == 9:
            table2[i, j] = 1
for value in range(8, -1, -1):
    for i in range(lenx):
        for j in range(leny):
            if x[i, j] == value:
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < lenx and 0 <= nj < leny and x[ni, nj] == value + 1:
                        table2[i, j] += table2[ni, nj]
print(np.sum(table2[x == 0]))








#p2 


