"""
이건 BFS로 돌리는게 좋을 것같다
단순하게 탐색하며 카운팅을 하는 문제
- 여기서 직선과 코너를 구분하는 로직을 올바르게 구현하는 게 중요할 것같음 (직선 100, 코너 500)
    -> 이전 변경이 x인지 y인지 boolean이나 int값으로 가지고 있는게 좋을 것같다.
    -> 아니면 일단 경로가 구해진 다음에 경로를 다시 순환하는 것도 방법일 수도?: 이건 너무 비효율적인가?
그런데 이거 보면 볼수록 다익스트라 문제같은데? 저번주에 우선순위 큐를 나중에 알려준다는게 이거 때문이셨나?

제한 사항
- 9-625 크기
- 0은 연결가능, 1은 불가능
- 건설 불가능 경우 x
- 출발점과 도착점은 항상 0
(중요!) 첫이동은 항상 100원

??? 왜 시간 초과가 난거지? 아하! ㅋㅋㅋㅋㅋㅋ
"""
from collections import deque

def solution(board):
    N = len(board)
    
    # (x, y)에 dir 방향으로 도착했을 때 최소 비용
    # 상:0 하:1 좌:2 우:3
    cost_map = [[[float('inf')] * 4 for _ in range(N)] for _ in range(N)]
    queue = deque()
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 우
    if board[0][1] == 0:
        cost_map[0][1][3] = 100  
        queue.append((0, 1, 3, 100)) 
    # 하
    if board[1][0] == 0:
        cost_map[1][0][1] = 100  
        queue.append((1, 0, 1, 100))

    while queue:
        x, y, prev_dir, current_cost = queue.popleft()
        
        for next_dir in range(4):
            nx, ny = x + dx[next_dir], y + dy[next_dir]
            
            # 맵 범위 체크
            if not (0 <= nx < N and 0 <= ny < N):
                continue
                
            # 벽 체크
            if board[nx][ny] == 1:
                continue
                
            # 비용 계산
            if prev_dir == next_dir:
                new_cost = current_cost + 100
            else:  # 코너
                new_cost = current_cost + 600
                
            # 비용 갱신 (= 조건 빼기 필수)
            if new_cost < cost_map[nx][ny][next_dir]:
                cost_map[nx][ny][next_dir] = new_cost
                queue.append((nx, ny, next_dir, new_cost))
                
    answer = min(cost_map[N-1][N-1])
    return answer