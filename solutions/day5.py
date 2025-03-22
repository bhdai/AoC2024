def parseInput(fileName):
    rules = []
    updates = []
    with open(fileName, 'r') as f:
        is_rules = True
        for line in f:
            if is_rules:
                if line == "\n":
                    is_rules = False
                    continue
                x, y = map(int, line.strip().split("|"))
                rules.append((x,y))
            else:
                updates.append(list(map(int, line.strip().split(","))))
    return rules, updates
                
rules, updates = parseInput("../inputs/day5_input.txt")

def graph(rules):
    graph = {}
    for x,y in rules:
        # create x, y node if it not extist
        if x not in graph: graph[x] = []
        if y not in graph: graph[y] = []
        graph[x].append(y) # direct x -> y
    return graph

def is_valid_update(graph, update):
    # convert update into position map for O(1) lookups
    position = {page: idx for idx, page in enumerate(update)}
    
    for page in position:
        if page in graph:
            for next_page in graph[page]:
                if next_page in position and position[next_page] < position[page]:
                    return False
    return True


def part1(rules, updates):
    g = graph(rules)
    valid_updates = []
    for update in updates:
        if is_valid_update(g, update):
            valid_updates.append(update)
    return sum(update[len(update)//2] for update in valid_updates)

def topological_sort(graph, nodes):
    subgraph = {node: [n for n in neighbors if n in nodes]
                for node, neighbors in graph.items() if node in nodes}

    # calculate in-degree of each node
    in_degree = {node: 0 for node in nodes}
    for node in subgraph:
        for neighbor in subgraph[node]:
            in_degree[neighbor] += 1

    queue = [node for node in nodes if in_degree[node] == 0]
    results = []

    while queue:
        node = queue.pop(0)
        results.append(node)
        for neighbor in subgraph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return results

def part2(rules, updates):
    g = graph(rules)
    total = 0
    for update in updates:
        if not is_valid_update(g, update):
            sorted_update = topological_sort(g, update)
            total += sorted_update[len(sorted_update)//2]

    return total

print(part2(rules, updates))
