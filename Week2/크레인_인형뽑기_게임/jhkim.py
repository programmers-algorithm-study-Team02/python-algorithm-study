def solution(board, moves):
    answer = 0
    bucket = []
    
    for move in moves:
        col = move -1
        for idx, line in enumerate(board):
            doll = line[col]
            if doll:
                if bucket and bucket[-1] == doll:
                    bucket.pop()
                    answer += 2
                else:
                    bucket.append(doll)
                board[idx][col] = 0
                break
    
    return answer