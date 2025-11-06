from collections import deque


def solution(n, m, hole):
    traps = set((x - 1, y - 1) for x, y in hole)
    start = (0, 0)
    goal = (n - 1, m - 1)

    if start in traps or goal in traps:
        return -1

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visited = [[[False] * 2 for _ in range(m)] for __ in range(n)]
    dq = deque()

    visited[0][0][0] = True
    dq.append((0, 0, 0, 0))

    while dq:
        x, y, used, dist = dq.popleft()
        if (x, y) == goal:
            return dist

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in traps:
                if not visited[nx][ny][used]:
                    visited[nx][ny][used] = True
                    dq.append((nx, ny, used, dist + 1))

        if used == 0:
            for dx, dy in dirs:
                nx, ny = x + 2 * dx, y + 2 * dy
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in traps:
                    if not visited[nx][ny][1]:
                        visited[nx][ny][1] = True
                        dq.append((nx, ny, 1, dist + 1))
    return -1