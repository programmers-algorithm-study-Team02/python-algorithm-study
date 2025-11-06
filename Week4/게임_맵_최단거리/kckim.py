from collections import deque

def solution(maps):
    
    def valid_pos(pos):
        return True if 0 <= pos[0] < len(maps) and 0 <= pos[1] < len(maps[0]) and maps[pos[0]][pos[1]] != 0 else False
    
    dst = (len(maps) - 1, len(maps[0]) - 1)
    visit = {(0, 0)}
    bfs = deque([((0, 0), 1)])
    while bfs:
        pos, time = bfs.popleft()
        
        if pos == dst:
            return time
        
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (pos[0] + di, pos[1] + dj)
            if valid_pos(new_pos) and new_pos not in visit:
                visit.add(new_pos)
                bfs.append((new_pos, time + 1))
    return -1
