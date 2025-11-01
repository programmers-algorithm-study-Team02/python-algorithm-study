from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])

    S = L = E = None

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                S = (i, j)
            elif maps[i][j] == 'L':
                L = (i, j)
            elif maps[i][j] == 'E':
                E = (i, j)
    if not (S and L and E):
        return -1

    def bfs(start, target):
        dist = [[-1] * m for _ in range(n)]
        q = deque([start])
        dist[start[0]][start[-1]] = 0
        while q:
            x, y = q.popleft()
            if (x, y) == target:
                return dist[x][y]
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] != 'X' and dist[nx][ny] == -1:
                        dist[nx][ny] = dist[x][y] + 1
                        q.append((nx, ny))
        return -1

    s_to_l = bfs(S, L)
    if s_to_l == -1: return -1
    l_to_e = bfs(L, E)
    if l_to_e == -1: return -1
    return s_to_l + l_to_e


