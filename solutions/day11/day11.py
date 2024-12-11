import numpy as np
import itertools
from collections import defaultdict
# lines = open('solutions/day11/sample.txt').read().splitlines()
lines = open('solutions/day11/input.txt').read().splitlines()

x = list(map(int, lines[0].split()))
stone_counts = {n: 1 for n in x}
def update(stone_counts):
    new_stones = defaultdict(int)
    for stone, count in stone_counts.items():
        if stone == 0:
            new_stones[1] += count
            continue
        if len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            left = stone_str[:len(stone_str)//2]
            right = stone_str[len(stone_str)//2:]
            left = int(left)
            right = int(right)
            new_stones[left] += count
            new_stones[right] += count
            continue
        else:
            new_stones[stone*2024] += count
            continue
    return new_stones
 
blinks = 75
for i in range(blinks):
    stone_counts = update(stone_counts)
    
print(sum(stone_counts.values()))
        
