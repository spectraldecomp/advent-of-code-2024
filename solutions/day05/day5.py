import numpy as np
from collections import defaultdict

lines = open('solutions/day05/sample.txt').read().splitlines()
# lines = open('solutions/day05/input.txt').read().splitlines()

orderings = defaultdict(list)
orders = []
for line in lines:
    if '|' in line:
        key, value = map(int, line.split('|'))
        orderings[key].append(value)
    if ',' in line:
        orders.append([int(num) for num in line.split(',')])

def ordered(order, orderings):
    for i in range(len(order)):
        num = order[i]
        vals = orderings[num]
        for val in vals:
            if val in order[:i]:
                return False
    return True

# part 1
sum = 0
for order in orders:
    if ordered(order, orderings):
        sum += order[len(order)//2]
print(f"Sum of middle values: {sum}")

# part 2
def fix(order, orderings):
    while not ordered(order, orderings):
        for i in range(len(order)):
            for j in range(i+1, len(order)):
                if order[i] in orderings[order[j]]:
                    order[i], order[j] = order[j], order[i]   
sum_bad = 0
for order in orders:
    if not ordered(order, orderings):
        fix(order, orderings)
        sum_bad += order[len(order)//2] 
print(f"Sum of incorrect middle values: {sum_bad}")


        
        
        
