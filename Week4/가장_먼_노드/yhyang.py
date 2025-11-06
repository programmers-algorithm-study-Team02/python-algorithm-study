from collections import deque

def solution(n, vertex):
    g = [[] for _ in range(n + 1)]
    for a, b in vertex:
        g[a].append(b)
        g[b].append(a)

    dist = [-1] * (n + 1)
    dist[1] = 0
    q = deque([1])

    while q:
        u = q.popleft()
        for v in g[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)

    far = max(dist[1:])

    return sum(d == far for d in dist[1:])


vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
n = 6
solution(n, vertex)