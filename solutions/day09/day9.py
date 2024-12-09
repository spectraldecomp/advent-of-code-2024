import numpy as np
import itertools
lines = open('solutions/day09/sample.txt').read().splitlines()
lines = open('solutions/day09/input.txt').read().splitlines()
lines = lines[0]
disk = []
id = 0
ct = 0
valid = True
while ct < len(lines):
    length = int(lines[ct])
    if valid:
        for _ in range(length):
            disk.append(str(id))
        id += 1
    else:
        for _ in range(length):
            disk.append('.')
    valid = not valid
    ct += 1
    
# print(disk)

# l = 0
# r = len(disk) - 1
# while l < r:
#     while l <= len(disk) and disk[l] != '.':
#         l += 1
#     while r >= 0 and disk[r] == '.':
#         r -= 1
    
#     if l < r:
#         disk[l], disk[r] = disk[r], disk[l]

# checksum = 0

# for i, char in enumerate(disk):
#     if char == '.':
#         break
#     checksum += i * int(char)
    
# print(checksum)

#p2

# print(disk)

for idx in range(id-1, 0, -1):
    # print(disk)
    # print("ID: ", idx)
    l = -1
    for i in range(len(disk)):
        if disk[i] == str(idx):
            l = i
            break
    
    r = l
    while r < len(disk) and disk[r] == str(idx):
        r += 1
        
    length = r - l
    
    # print("l: ", l)
    # print("r: ", r)
    # print("Length: ", length)
    
    for lf in range(l - length + 1):
        # Make sure the space is all '.'
        if all([disk[lf + i] == '.' for i in range(length)]):
            # print("Space is all 0s at ", lf, " to ", lf + length)
            # print("Setting ", lf, " to ", lf + length, " to ", idx)
            for j in range(length):
                disk[lf + j] = str(idx)
            # print("Setting ", l, " to ", r, " to '.'")
            for j in range(l, r):
                disk[j] = '.'
                
            break

# print(disk)
    
checksum = 0
for i, char in enumerate(disk):
    if char == '.':
        continue
    checksum += i * int(char)

print(checksum)


