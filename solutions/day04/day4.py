import numpy as np


lines = open('solutions/day04/sample.txt').read().splitlines()
lines = open('solutions/day04/input.txt').read().splitlines()
slines = [list(line) for line in lines]
x = np.array(slines)

print(x)

# Pad array with # to avoid index out of bounds
x = np.pad(x, 1, constant_values='#')
print(x)


# part 1

XMAS_count = 0
visited = set()

for i in range(1, len(x)-1):
    for j in range(1, len(x[i])-1):
        # Skip if we've already visited this cell
        if (i, j) in visited:
            continue
        # Check to see if XMAS occurs to the right
        if x[i][j] == 'X' and x[i][j+1] == 'M' and x[i][j+2] == 'A' and x[i][j+3] == 'S':
            XMAS_count += 1
            visited.add((i, j))
        # Check to see if XMAS occurs backwards
        if x[i][j] == 'X' and x[i][j-1] == 'M' and x[i][j-2] == 'A' and x[i][j-3] == 'S':
            XMAS_count += 1
            visited.add((i, j))
        # Check to see if XMAS occurs below
        if x[i][j] == 'X' and x[i+1][j] == 'M' and x[i+2][j] == 'A' and x[i+3][j] == 'S':
            XMAS_count += 1
            visited.add((i, j))
        # Check to see if XMAS occurs above
        if x[i][j] == 'X' and x[i-1][j] == 'M' and x[i-2][j] == 'A' and x[i-3][j] == 'S':
            XMAS_count += 1
            visited.add((i, j))
            
        # Check diagonals
        
        # Check to see if XMAS occurs to the right and below
        if x[i][j] == 'X' and x[i+1][j+1] == 'M' and x[i+2][j+2] == 'A' and x[i+3][j+3] == 'S':
            XMAS_count += 1
            visited.add((i, j))
        # Check to see if XMAS occurs to the right and above
        if x[i][j] == 'X' and x[i-1][j+1] == 'M' and x[i-2][j+2] == 'A' and x[i-3][j+3] == 'S':
            XMAS_count += 1
            visited.add((i, j))
        # Check to see if XMAS occurs to the left and below
        if x[i][j] == 'X' and x[i+1][j-1] == 'M' and x[i+2][j-2] == 'A' and x[i+3][j-3] == 'S':
            XMAS_count += 1
            visited.add((i, j))
        # Check to see if XMAS occurs to the left and above
        if x[i][j] == 'X' and x[i-1][j-1] == 'M' and x[i-2][j-2] == 'A' and x[i-3][j-3] == 'S':
            XMAS_count += 1
            visited.add((i, j))
        
print(XMAS_count)

# part 2
MAS_count = 0
visited = set()

for i in range(1, len(x)-1):
    for j in range(1, len(x[i])-1):
        # Skip if we've already visited this cell
        if (i, j) in visited:
            continue
        
        if x[i][j] == 'A':
            good = True
            if x[i-1][j-1] == 'M':
                if x[i+1][j+1] == 'M':
                    good = False
            elif x[i-1][j+1] == 'M':
                if x[i+1][j-1] == 'M':
                    good = False
            elif x[i-1][j-1] == 'S':
                if x[i+1][j+1] == 'S':
                    good = False
            elif x[i-1][j+1] == 'S':
                if x[i+1][j-1] == 'S':
                    good = False
            # Check to make sure the 4 diagonals are 2 M's and 2 S's
            m_count = 0
            s_count = 0
            if x[i-1][j-1] == 'M':
                m_count += 1
            elif x[i-1][j-1] == 'S':
                s_count += 1
            if x[i-1][j+1] == 'M':
                m_count += 1
            elif x[i-1][j+1] == 'S':
                s_count += 1
            if x[i+1][j-1] == 'M':
                m_count += 1
            elif x[i+1][j-1] == 'S':
                s_count += 1
            if x[i+1][j+1] == 'M':
                m_count += 1
            elif x[i+1][j+1] == 'S':
                s_count += 1
            if m_count != 2 or s_count != 2:
                good = False
            
            if good:
                visited.add((i, j))
                MAS_count += 1
                
print(MAS_count)
                
                
                
                
                    


        