from collections import deque

def solution(board):
    dst = len(board) - 1
    max_cost = 500 * dst ** 2
    cost_board = [[[max_cost] * 4 for _ in range(len(board))] for _ in range(len(board))]
    
    def valid_pos(pos):
        i, j = pos
        return True if 0 <= i <= dst and 0 <= j <= dst and board[i][j] == 0 else False
    
    def get_new_pos(pos, direction):
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return (pos[0] + dirs[direction][0], pos[1] + dirs[direction][1])

    bfs = deque([((0, 0), 0, 0)])

    while bfs:
        pos, cost, old_dir = bfs.popleft()

        for new_dir in range(4):
            new_cost = cost + 100 if pos == (0, 0) or old_dir == new_dir else cost + 600
            ni, nj = get_new_pos(pos, new_dir)
            if valid_pos((ni, nj)) and new_cost < cost_board[ni][nj][new_dir]:
                bfs.append(((ni, nj), new_cost, new_dir))
                cost_board[ni][nj][new_dir] = new_cost

    answer = min(cost_board[dst][dst])
        
    return answer
