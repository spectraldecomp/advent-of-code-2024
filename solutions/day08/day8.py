import numpy as np
import itertools
# lines = open('solutions/day08/sample.txt').read().splitlines()
lines = open('solutions/day08/input.txt').read().splitlines()

x = np.array([list(line) for line in lines])
lenx,leny = x.shape


frequencies = set(x.flatten())
frequencies.remove('.')
coords = []
for freq in frequencies:
    coord = set()
    for i, line in enumerate(x):
        for j, c in enumerate(line):
            if c == freq:
                coord.add((i,j))
    coords.append(coord)
    

def an(c1,c2):
    x1,y1 = c1
    x2,y2 = c2
    x = 2*x1-x2
    y = 2*y1-y2
    if 0 <= x < lenx and 0 <= y < leny:
        return {(x,y)}
    return set()

def an2(c1,c2):
    x1,y1 = c1
    x2,y2 = c2
    dx,dy = x2-x1,y2-y1
    res = set()
    x_tmp, y_tmp = x1, y1
    while 0 <= x_tmp < lenx and 0 <= y_tmp < leny:
        res.add((x_tmp, y_tmp))
        x_tmp += dx
        y_tmp += dy
    x_tmp, y_tmp = x1, y1
    while 0 <= x_tmp < lenx and 0 <= y_tmp < leny:
        res.add((x_tmp, y_tmp))
        x_tmp -= dx
        y_tmp -= dy
    return res

anodes = set()
for c in coords:
    for c1,c2 in itertools.permutations(c,2):
        anodes.update(an(c1,c2))
print(len(anodes))

anodes = set()
for c in coords:
    for c1,c2 in itertools.permutations(c,2):
        anodes.update(an2(c1,c2))
        

print(len(anodes))