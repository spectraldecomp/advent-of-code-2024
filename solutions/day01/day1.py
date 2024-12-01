import numpy as np

lines = open('solutions/day01/sample.txt').read().splitlines()
lines = open('solutions/day01/input.txt').read().splitlines()

left = []
right = []
for line in lines:
    left.append(int(line.split()[0]))
    right.append(int(line.split()[1]))
left.sort()
right.sort()

# day 1
differences = []
for i in range(len(left)):
    differences.append(abs(left[i] - right[i]))
    
print(sum(differences))

# day 2
total = 0
for number in left:
    freq = right.count(number)
    total += freq * number
    
print(total)