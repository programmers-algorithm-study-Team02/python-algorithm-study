from collections import deque

def solution(maps):
    S, L, E = find_SLE(maps)
    
    StoL = get_short_len_path(maps, S, L)
    LtoE = get_short_len_path(maps, L, E)
    
    if StoL == -1 or LtoE == -1:
        return -1
    
    return StoL + LtoE

def get_short_len_path(maps, src, dst):
    visit = {src}
    bfs = deque([(src, 0)])
    
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    while bfs:
        pos, time = bfs.popleft()
        
        if pos == dst:
            return time
        
        for n in range(4):
            next_pos = (pos[0] + di[n], pos[1] + dj[n])
            if valid_pos(maps, next_pos) and maps[next_pos[0]][next_pos[1]] != 'X':
                if next_pos not in visit:
                    bfs.append((next_pos, time + 1))
                    visit.add(next_pos)
    return -1

def find_SLE(maps):
    S, L, E = 0, 0, 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                S = (i, j)
            elif maps[i][j] == 'L':
                L = (i, j)
            elif maps[i][j] == 'E':
                E = (i, j)
    return (S, L, E)

def valid_pos(maps, pos):
    if pos[0] >= len(maps) or pos[0] < 0 or pos[1] >= len(maps[0]) or pos[1] < 0:
        return False
    return True
