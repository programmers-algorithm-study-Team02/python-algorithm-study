def solution(k, dungeons):
    n = len(dungeons)
    best = 0

    def dfs(cur, visited, clear):
        nonlocal best
        best = max(best, clear)

        for i in range(n):
            if not (visited & (1 << i)):
                need, cost = dungeons[i]
                if cur >= need:
                    dfs(cur - cost, visited | (1 << i), clear + 1)

    dfs(k, 0, 0)

    return best