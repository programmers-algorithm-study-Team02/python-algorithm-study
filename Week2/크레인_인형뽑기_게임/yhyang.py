def solution(board, moves):
    answer = 0 # 터진 인형 갯수를 저장
    basket = [] # 인형을 저장
    n = len(board) # 보드의 크기

    for move in moves:
        col = move - 1 #  move[0]이 1번 움직임이므로 - 1
        for row in range(n):
            if board[row][col] != 0: # 해당 행열이 0이 아니라면 인형은 해당 번호
                doll = board[row][col]
                board[row][col] = 0 # else에서 인형을 넣고 0으로 초기화

                if basket and basket[-1] == doll: # basket이 빈 배열이 아니고 마지막 저장이 인형과 같다면
                    basket.pop() # 인형을 지움
                    answer += 2 # 2개가 붙어야 터지므로 2개씩 갯수를 올림
                else:
                    basket.append(doll) # 아니라면 인형을 basket에 저장
                break
    return answer

# 시간 복잡도 O(M * n)