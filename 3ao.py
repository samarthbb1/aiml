
graph = {
    'A': [[('B', 1), ('C', 1)], [('D', 2)]],
    'B': [[('E', 2)]],
    'C': [[('F', 2)]],
    'D': [[('G', 1)]],
    'E': [],
    'F': [],
    'G': []
}

heuristic = {
    'A': 4,
    'B': 2,
    'C': 2,
    'D': 2,
    'E': 0,
    'F': 0,
    'G': 0
}

solved = set()
solution = {}

def ao_star(node):
    if node not in graph or not graph[node]:
        solved.add(node)
        return heuristic[node]

    best_cost = float('inf')
    best_option = None

    for option in graph[node]:
        cost = 0

        for child, edge_cost in option:
            cost += edge_cost + ao_star(child)

        if cost < best_cost:
            best_cost = cost
            best_option = option

    heuristic[node] = best_cost
    solution[node] = best_option
    solved.add(node)

    return best_cost


def print_solution(node, level=0):
    print(" " * level + node)

    if node in solution:
        for child, cost in solution[node]:
            print_solution(child, level + 1)


cost = ao_star('A')

print("Minimum Cost:", cost)
print("\nSolution Graph:")
print_solution('A')
