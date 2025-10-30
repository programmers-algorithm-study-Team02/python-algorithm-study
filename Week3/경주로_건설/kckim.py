from collections import deque

def solution(board):
    dst = len(board) - 1
    max_cost = 500 * dst ** 2
    cost_board = [[[max_cost] * len(board) for _ in range(len(board))] for _ in range(4)]
    
    def valid_pos(pos):
        i, j = pos
        return True if 0 <= i <= dst and 0 <= j <= dst and board[i][j] == 0 else False
    
    def construct_course():
        # pos, cost, dir
        bfs = deque([((0, 0), 0, 0)])
        
        def get_new_pos(pos, direction):
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            i, j = pos
            di, dj = dirs[direction]
            return (i + di, j + dj)
        
        while bfs:
            pos, cost, old_dir = bfs.popleft()
            i, j = pos
            if cost > cost_board[old_dir][i][j]:
                continue
            
            for new_dir in range(4):
                corner = 0
                if pos != (0, 0) and old_dir != new_dir:
                    corner = 500
                
                new_pos = get_new_pos(pos, new_dir)
                ni, nj = new_pos
                new_cost = cost + 100 + corner
                if valid_pos(new_pos) and new_cost < cost_board[new_dir][ni][nj]:
                    bfs.append((new_pos, new_cost, new_dir))
                    cost_board[new_dir][ni][nj] = new_cost
        
    construct_course()
    answer = cost_board[0][dst][dst]
    for i in range(4):
        answer = min(answer, cost_board[i][dst][dst])
        
    return answer
