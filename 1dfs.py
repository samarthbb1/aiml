
def water_jug_dfs(capacity1, capacity2, target):
    visited = set()
    path = []

    def dfs(x, y):
        if (x, y) in visited:
            return False

        visited.add((x, y))
        path.append((x, y))

        if x == target or y == target:
            return True

        states = [
            (capacity1, y),
            (x, capacity2),
            (0, y),
            (x, 0)
        ]

        n = min(x, capacity2 - y)
        states.append((x - n, y + n))

        n = min(y, capacity1 - x)
        states.append((x + n, y - n))

        for a, b in states:
            if dfs(a, b):
                return True

        path.pop()
        return False

    if dfs(0, 0):
        print("Solution Path:")
        for state in path:
            print(state)
    else:
        print("No solution exists.")


capacity1 = int(input("Enter capacity of Jug 1: "))
capacity2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))

water_jug_dfs(capacity1, capacity2, target)
