"""
이건 레버라는 필수경로를 제외하면 단순한 최단 경로 문제로 BFS로 푸는 것이 좋을 것같다.
경로를 분리하자 
 1. 시작점 - 레버
 2. 레버 - 탈출구
"""
def find_path(start, target, maps):
    rows = len(maps)
    cols = len(maps[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = []

    sx, sy = start
    queue.append((sx, sy, 0))
    visited[sx][sy] = True

    while queue:
        x, y, direc = queue.pop(0)
        
        if (x, y) == target:
            return direc
    
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            # 진행 가능여부 체크(범위, 벽, 중복방문)
            if 0 <= nx < rows and 0 <= ny < cols and maps[nx][ny] != 'X' and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, direc + 1))
                
    return -1 # 경로 없는 경우

def solution(maps):
    start = None
    lever = None
    exit = None
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                exit = (i, j)

    # 시작점 - 레버 
    path_to_lever = find_path(start, lever, maps)

    # 레버 - 탈출구
    path_to_exit = find_path(lever, exit, maps)

    if path_to_lever == -1 or path_to_exit == -1:
        return -1
    else:
        return path_to_lever + path_to_exit