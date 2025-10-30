"""
어우...
일단 제한사항 5번 때문에 정렬이 필요할 테니 정렬부터 시키자
1. 사전 순 정렬
2. 탐색
    - 티켓이 모두 소진되지 않는다면 백트레킹
    - 경로가 없다면 None
    - 성공하면 경로 return
(중요!) 시작은 무조건 ICN + 모든 도시를 방문 못하는 경우 x
"""
def dfs(start, path, tickets, visited):
    # 성공 조건
    if len(path) == len(tickets) + 1:
        return path 

    # 티켓 순회
    for idx, ticket in enumerate(tickets):
        if ticket[0] == start and not visited[idx]:
            visited[idx] = True
            # 공항탐색
            result_path = dfs(ticket[1], path + [ticket[1]], tickets, visited)
            
            # 성공
            if result_path:
                return result_path
            # 실패 -> 백트래킹
            visited[idx] = False
            
    # 경로x
    return None

def solution(tickets):
    tickets.sort(key=lambda x: (x[0], x[1]))
    visited = [False] * len(tickets)
    answer = dfs("ICN", ["ICN"], tickets, visited)
    return answer