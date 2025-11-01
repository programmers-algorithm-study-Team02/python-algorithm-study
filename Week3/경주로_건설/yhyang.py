import heapq


def solution(board):
    n = len(board)
    INF = 10 ** 15
    cost = [[[INF] * 4 for _ in range(n)] for __ in range(n)]

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    pq = []

    for ndir, (dx, dy) in enumerate(dirs):
        nx, ny = 0 + dx, 0 + dy
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
            cost[nx][ny][ndir] = 100
            heapq.heappush(pq, (100, nx, ny, ndir))

    while pq:
        cur_cost, x, y, d = heapq.heappop(pq)
        if cur_cost > cost[x][y][d]:
            continue

        if x == n - 1 and y == n - 1:
            return cur_cost

        for ndir, (dx, dy) in enumerate(dirs):
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if board[nx][ny] == 1:
                continue

            add = 100 if ndir == d else 600
            ncost = cur_cost + add
            if ncost < cost[nx][ny][ndir]:
                cost[nx][ny][ndir] = ncost
                heapq.heappush(pq, (ncost, nx, ny, ndir))

    return -1