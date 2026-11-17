
from collections import deque

def bfs(m, c):
    start = (m, c, 0)
    goal = (0, 0, 1)

    moves = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        m1, c1, boat = state

        for dm, dc in moves:
            if boat == 0:
                nm, nc, nb = m1-dm, c1-dc, 1
            else:
                nm, nc, nb = m1+dm, c1+dc, 0

            if not (0 <= nm <= m and 0 <= nc <= c):
                continue

            rm, rc = m-nm, c-nc

            if (nm > 0 and nm < nc) or (rm > 0 and rm < rc):
                continue

            nxt = (nm, nc, nb)

            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path + [nxt]))

    return None


m = int(input("Enter no. of Missionaries: "))
c = int(input("Enter no. of Cannibals: "))

path = bfs(m, c)

if path:
    print("\nBFS Solution:")
    for state in path:
        print(state)
else:
    print("No solution found.")
