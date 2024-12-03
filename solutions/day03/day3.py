import re

lines = open('solutions/day03/input.txt').read().splitlines()

x = []

for _, line in enumerate(lines):
    # mul, paren, 1-3 digit number , comma, 1-3 digit number, paren, or do() or don't()
    x.append(re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)', line))

product = 0
valid = True
for line in x:
    for instruction in line:
        if instruction == "do()":
            valid = True
        elif instruction == "don't()":
            valid = False
        elif valid:
            product += int(instruction.split(',')[0][4:]) * int(instruction.split(',')[1][:-1])
print(product)


