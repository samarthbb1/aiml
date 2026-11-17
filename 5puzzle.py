import heapq

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def manhattan(state):
    total = 0

    for i, v in enumerate(state):
        if v == 0:
            continue

        gi = GOAL.index(v)

        total += abs(i//3 - gi//3) + abs(i%3 - gi%3)

    return total

def neighbors(state):
    z = state.index(0)
    r, c = divmod(z, 3)

    for dr, dc, move in [
        (-1, 0, "Up"),
        (1, 0, "Down"),
        (0, -1, "Left"),
        (0, 1, "Right")
    ]:
        nr, nc = r+dr, c+dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            nz = nr*3 + nc
            s = list(state)

            s[z], s[nz] = s[nz], s[z]

            yield tuple(s), move

def a_star_puzzle(start):
    pq = [(manhattan(start), 0, start)]
    g = {start: 0}
    parent = {start: (None, None)}

    while pq:
        f, cost, state = heapq.heappop(pq)

        if state == GOAL:
            path = []

            while parent[state][0] is not None:
                prev, move = parent[state]
                path.append((move, state))
                state = prev

            return path[::-1]

        if cost != g[state]:
            continue

        for nxt, move in neighbors(state):
            new_cost = cost + 1

            if nxt not in g or new_cost < g[nxt]:
                g[nxt] = new_cost
                parent[nxt] = (state, move)

                heapq.heappush(
                    pq,
                    (new_cost + manhattan(nxt), new_cost, nxt)
                )

    return None

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)

path = a_star_puzzle(start)

print("A* Solution:")
print("Start:", start)

if path is not None:
    for i, (move, state) in enumerate(path, 1):
        print(f"Move {i}: {move} -> {state}")

    print("Number of moves:", len(path))
else:
    print("No solution found.")