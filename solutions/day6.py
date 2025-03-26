DIRECTIONS = ['^', '>', 'v', '<']
DIRECTION_MAP = { '^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1) }

def parse_input(file_name) : return [line.strip() for line in open(file_name)]

def find_guard_position(map, rows, cols, direct_map):
    for i in range(rows):
        for j in range(cols):
            if map[i][j] in direct_map:
                return ( i, j )
    raise ValueError('No guard found in the map')

def part1(map):
    rows, cols = len(map), len(map[0])
    i, j = find_guard_position(map, rows, cols, DIRECTION_MAP)
    dr = DIRECTIONS.index(map[i][j])
    visisted = {(i,j)}

    while True:
        next_i, next_j= i + DIRECTION_MAP[DIRECTIONS[dr]][0],j + DIRECTION_MAP[DIRECTIONS[dr]][1]
        if not (0 <= next_i < rows and 0 <= next_j < cols): break
        if map[next_i][next_j] == '#': # check if there an obstacle ahead
            # turn right
            dr = (dr + 1) % 4
        else:
            # move forward
            i, j = next_i, next_j
            visisted.add((i,j))
    return len(visisted)

def simulation_guard_movement(map, rows, cols, guard_pos, obstacle_pos):
    ox, oy = obstacle_pos

    if map[ox][oy] != '.' or obstacle_pos == guard_pos: return None

    obstacles = { (x, y) for x in range(rows) for y in range(cols) if map[x][y] == '#' }
    obstacles.add(obstacle_pos)

    i, j = guard_pos
    dr = DIRECTIONS.index(map[i][j])

    visisted = set()
    path = []

    while True:
        # store the current state
        state = (i, j, dr)
        if state in visisted: return path # WE FOUND A LOOP!
        visisted.add(state)
        path.append((i,j))
        next_i, next_j = i + DIRECTION_MAP[DIRECTIONS[dr]][0], j + DIRECTION_MAP[DIRECTIONS[dr]][1]
        if not (0 <= next_i < rows and 0 <= next_j < cols): return None
        if (next_i, next_j) in obstacles: dr = (dr + 1) % 4
        else: i, j = next_i, next_j

def part2(map):
    rows, cols = len(map), len(map[0])
    valid_position = []
    guard_pos = find_guard_position(map, rows, cols, DIRECTION_MAP)

    for i in range(rows):
        for j in range(cols):
            if map[i][j] == '.':
                path = simulation_guard_movement(map, rows, cols, guard_pos, (i,j))
                if path is not None: valid_position.append((i,j))
    return len(valid_position)

pos_map = parse_input('../inputs/day6_input.txt')
rows = len(pos_map)
cols = len(pos_map[0])

print(part2(pos_map))
