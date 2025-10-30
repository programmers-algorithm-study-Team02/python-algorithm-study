"""
이것도 푼 적 있는 문제네?
이거는 주어진 computers를 이용해 DFS, BFS로 카운팅을 하는 문제네
그런데 이거 n은 굳이 필요없지 않나? 그리고 이게 왜 lv3인거지?
간결하게 DFS로 하자
"""
import sys
sys.setrecursionlimit(10**6)  # n이 depth 상한인 200이기에 추가

def dfs(node, n, computers, visited):
    visited[node] = True
    for neighbor in range(n):
        if computers[node][neighbor] == 1 and not visited[neighbor]:
            dfs(neighbor, n, computers, visited)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    # 그래프 돌면서 dfs
    for i in range(n):
        if not visited[i]:
            dfs(i, n, computers, visited) 
            answer += 1
            
    return answer