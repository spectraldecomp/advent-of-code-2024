from itertools import product

lines = open('solutions/day07/sample.txt').read().splitlines()
# lines = open('solutions/day07/input.txt').read().splitlines()


def evaluate_left_to_right(nums, ops):
    """Evaluate an expression left-to-right using the given numbers and operators."""
    result = nums[0]
    for num, op in zip(nums[1:], ops):
        if op == '+':
            result += num
        elif op == '*':
            result *= num
        elif not p1 and op == '||':
            result = int(str(result) + str(num))
    return result

p1 = True
sum_valid = 0
for line in lines:
    parts = line.split(':')
    target = int(parts[0].strip())
    nums = list(map(int, parts[1].strip().split()))
    
    operators = ['+', '*', '||']
    valid = False
    for ops in product(operators, repeat=len(nums) - 1):
        if evaluate_left_to_right(nums, ops) == target:
            valid = True
            break
    if valid:
        sum_valid += target
print(sum_valid)
