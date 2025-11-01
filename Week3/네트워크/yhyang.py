def solution(n, computers):
    visited = [False] * n
    answer = 0

    def dfs(node):
        visited[node] = True
        for next_node in range(n):
            if computers[node][next_node] == 1 and not visited[next_node]:
                dfs(next_node)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1

    return answer