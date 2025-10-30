"""
이전에 푼적있는 문제네?
그림만 봐도 BFS문제. 그냥 탐색하며 값만 더하면 되는 단순한 문제
만약 상하좌우로 연결되지 않았다면 다른 섬으로 판단 후 바로 저장을 하면 되겠다
그런데 생각해보니 크게 차이가 날 것같진 않은데 DFS가 더 편할 것같다
"""
import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, maps, visited, row, col):
    if not (0 <= x < row and 0 <= y < col and maps[x][y] != 'X' and not visited[x][y]):
        return 0
        
    visited[x][y] = True
    food = int(maps[x][y])
    
    # 상하좌우 재귀
    food += dfs(x + 1, y, maps, visited, row, col)
    food += dfs(x - 1, y, maps, visited, row, col)
    food += dfs(x, y + 1, maps, visited, row, col)
    food += dfs(x, y - 1, maps, visited, row, col)
    
    return food

def solution(maps):
    row = len(maps)
    col = len(maps[0])
    visited = [[False] * col for _ in range(row)]
    answer = []
    
    for i in range(row):
        for j in range(col):
            # 새로운 섬의 시작점
            if maps[i][j] != 'X' and not visited[i][j]:
                island_sum = dfs(i, j, maps, visited, row, col)
                answer.append(island_sum)
                
    if not answer:
        return [-1]
    else:
        return sorted(answer)