def parse_input(input_data):
    machines = []
    lines = [line.strip() for line in input_data.strip().split("\n") if line.strip()]
    for i in range(0, len(lines), 3):
        a_line = lines[i].split(":")[1].strip()
        a_x, a_y = map(int, a_line.replace("X+", "").replace("Y+", "").split(", "))
        
        b_line = lines[i + 1].split(":")[1].strip()
        b_x, b_y = map(int, b_line.replace("X+", "").replace("Y+", "").split(", "))
        
        prize_line = lines[i + 2].split(":")[1].strip()
        p_x, p_y = map(int, prize_line.replace("X=", "").replace("Y=", "").split(", "))
        
        machines.append(((a_x, a_y), (b_x, b_y), (p_x, p_y)))
    return machines


def linear(P_x, P_y, x_1, x_2, y_1, y_2):
    # Find A inverse where A = [[x1, x2], [y1, y2]].
    # inverse is 1/det(A) * [[y2, -x2], [-y1, x1]]
    # = 1/(x1*y2 - x2*y1) * [[y2, -x2], [-y1, x1]]
    # = [[y2, -x2], [-y1, x1]] / (x1*y2 - x2*y1)
    # So v = A^-1b is solved W
    
    # See the linear.png for more details
    
    a = (P_x * y_2 - P_y * x_2) / (x_1 * y_2 - x_2 * y_1)
    b = (P_x * y_1 - P_y * x_1) / (x_2 * y_1 - x_1 * y_2)
    return a, b


input_data = open('solutions/day13/input.txt').read()
machines = parse_input(input_data)

#p1 
sum_tokens = 0
for idx, ((x_1, y_1), (x_2, y_2), (P_x, P_y)) in enumerate(machines):
    a, b = linear(P_x, P_y, x_1, x_2, y_1, y_2)
    if a >= 0 and b >= 0 and a.is_integer() and b.is_integer():
        tokens = a * 3 + b * 1
        sum_tokens += tokens
        print(f"Machine {idx + 1}: a = {a}, b = {b}, Tokens = {tokens}")
    else:
        print(f"Machine {idx + 1}: Nope")
    
print(f"Total tokens: {int(sum_tokens)}")

#p2

sum_tokens = 0
for idx, ((x_1, y_1), (x_2, y_2), (P_x, P_y)) in enumerate(machines):
    a, b = linear(P_x+10000000000000, P_y+10000000000000, x_1, x_2, y_1, y_2)
    if a >= 0 and b >= 0 and a.is_integer() and b.is_integer():
        tokens = a * 3 + b * 1
        sum_tokens += tokens
        print(f"Machine {idx + 1}: a = {a}, b = {b}, Tokens = {tokens}")
    else:
        print(f"Machine {idx + 1}: Nope")
    
print(f"Total tokens: {int(sum_tokens)}")
