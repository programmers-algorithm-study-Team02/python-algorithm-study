from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    answers = []

    def bfs(sx, sy):
        q = deque([(sx, sy)])
        visited[sx][sy] = True
        total = int(maps[sx][sy])

        while q:
            x, y = q.popleft()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and maps[nx][ny] != 'X':
                        visited[nx][ny] = True
                        total += int(maps[nx][ny])
                        q.append((nx, ny))
        return total

    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                answers.append(bfs(i, j))

    return sorted(answers) if answers else [-1]