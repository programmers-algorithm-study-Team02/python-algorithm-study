from collections import deque

def solution(n, m, holes):
    map = [[[float("inf")] * 2 for _ in range(m)] for _ in range(n)]
    
    for hole in holes:
        map[hole[0] - 1][hole[1] - 1][0] = -1
        map[hole[0] - 1][hole[1] - 1][1] = -1
    
    def valid_pos(pos):
        x, y = pos
        return True if 0 <= x < n and 0 <= y < m and map[x][y][0] != -1 else False
    
    dst = (n - 1, m - 1)
    bfs = deque([((0, 0), False, 0)])
        
    while bfs:
        pos, jump, time = bfs.popleft()
        if pos == dst:
            return time
        
        time += 1
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = pos[0] + dx, pos[1] + dy
            new_pos = (nx, ny)
            jump_idx = 1 if jump else 0
            if valid_pos(new_pos) and time < map[nx][ny][jump_idx]:
                map[nx][ny][jump_idx] = time
                bfs.append((new_pos, jump, time))
                
            if not jump:
                nx, ny = pos[0] + dx * 2, pos[1] + dy * 2
                new_pos = (nx, ny)
                if valid_pos(new_pos) and time < min(map[nx][ny]):
                    map[nx][ny][1] = time
                    bfs.append((new_pos, True, time))
    
    return -1
