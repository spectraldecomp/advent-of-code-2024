def parse_input(map_str, moves_str):
    warehouse = [list(line) for line in map_str.strip().split("\n")]
    moves = moves_str.replace("\n", "")
    return warehouse, moves



    
def process(warehouse):
    robot_pos = None
    boxes = set()
    for r, row in enumerate(warehouse):
        for c, cell in enumerate(row):
            if cell == "@":
                robot_pos = (r, c)
            elif cell == "O":
                boxes.add((r, c))
    return robot_pos, boxes

def move_robot(warehouse, robot_pos, boxes, direction):
    directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    dr, dc = directions[direction]
    new_robot_pos = (robot_pos[0] + dr, robot_pos[1] + dc)

    if new_robot_pos in boxes:
        box_chain = [new_robot_pos]
        next_box_pos = (new_robot_pos[0] + dr, new_robot_pos[1] + dc)
        
        while next_box_pos in boxes:
            box_chain.append(next_box_pos)
            next_box_pos = (next_box_pos[0] + dr, next_box_pos[1] + dc)
        could_move = True
        for i in range(len(box_chain) - 1, -1, -1):
            current_box_pos = box_chain[i]
            next_box_pos = (current_box_pos[0] + dr, current_box_pos[1] + dc)

            if (0 <= next_box_pos[0] < len(warehouse) and 0 <= next_box_pos[1] < len(warehouse[0]) and
                            warehouse[next_box_pos[0]][next_box_pos[1]] != "#" and next_box_pos not in boxes):
                boxes.remove(current_box_pos)
                boxes.add(next_box_pos)
                
                warehouse[current_box_pos[0]][current_box_pos[1]] = " "
                warehouse[next_box_pos[0]][next_box_pos[1]] = "O"
                
            else:
                could_move = False
                break
        if not could_move:
            return robot_pos
            
        robot_pos = box_chain[0]
    elif warehouse[new_robot_pos[0]][new_robot_pos[1]] != "#" and new_robot_pos not in boxes:
        robot_pos = new_robot_pos
        
    warehouse[robot_pos[0]][robot_pos[1]] = "@"
    
    prev_r, prev_c = robot_pos
    if warehouse[prev_r][prev_c] == "@":
        warehouse[prev_r][prev_c] = " "

    return robot_pos

def visualize_warehouse(warehouse, robot_pos, boxes):
    warehouse_copy = [list(row) for row in warehouse]
    for r in range(len(warehouse_copy)):
        for c in range(len(warehouse_copy[r])):
            if warehouse_copy[r][c] == "@":
                warehouse_copy[r][c] = " "

    robot_r, robot_c = robot_pos
    warehouse_copy[robot_r][robot_c] = "@"
    for box_r, box_c in boxes:
        warehouse_copy[box_r][box_c] = "O"
    for row in warehouse_copy:
        print("".join(row))



        




def simulate(map_str, moves_str):
    warehouse, moves = parse_input(map_str, moves_str)
    rows, cols = len(warehouse), len(warehouse[0])
    robot_pos, boxes = process(warehouse)
    print("Initial state:")
    visualize_warehouse(warehouse, robot_pos, boxes)
    for move in moves:
        # print("Move:", move)
        robot_pos = move_robot(warehouse, robot_pos, boxes, move)
        # visualize_warehouse(warehouse, robot_pos, boxes)

    return sum(100 * r + c for r, c in boxes)


input = open('solutions/day15/sample.txt').read()
input = open('solutions/day15/input.txt').read()
map, moves = input.split("\n\n")

# Run simulation
result = simulate(map, moves)
print("p1", result)
