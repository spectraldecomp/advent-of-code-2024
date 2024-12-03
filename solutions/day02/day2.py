import numpy as np


# lines = open('solutions/day02/sample.txt').read().splitlines()
lines = open('solutions/day02/input.txt').read().splitlines()
slines = [list(map(int, line.split())) for line in lines]

total = 0
def is_valid(line):
    diffs = True
    increasing_or_descending = (line == sorted(line)) or (line == sorted(line, reverse=True))
    for i in range(len(line)-1):
        diff = abs(line[i] - line[i+1])
        if not 1 <= diff <= 3:
            diffs = False
    return increasing_or_descending and diffs


# part 1
for line in slines:
    if is_valid(line):
        total += 1
        
print(total)


# part 2
for line in slines:
    valid = False
    for i in range(len(line)):
        # Check each line with one number removed
        if is_valid(line[:i] + line[i+1:]):
            valid = True
            break
    if valid:
        total += 1
        
print(total)
            
    
