def solution(board, moves):
    count = 0
    res = []
    
    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1] != 0:     # 인형이 있는 경우
                doll = board[i][move - 1]
                board[i][move - 1] = 0      # 인형 잡은 후 0으로 변경
                
                if res and res[-1] == doll:
                    res.pop()
                    count += 2
                else:
                    res.append(doll)
                break                        # 한번 인형 잡은 후 반복 종료
                    
    return count