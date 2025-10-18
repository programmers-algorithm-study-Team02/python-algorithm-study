def solution(keyinput, board):
    answer = [0, 0]
    if not keyinput:
        return [0, 0]
    for k in range(len(keyinput)):
        if keyinput[k] == "up":
            answer[1] = min(answer[1] + 1, board[1] // 2)
        elif keyinput[k] == "down":
            answer[1] = max(answer[1] - 1, -(board[1] // 2))
        elif keyinput[k] == "left":
            answer[0] = max(answer[0] - 1, -(board[0] // 2))
        elif keyinput[k] == "right":
            answer[0] = min(answer[0] + 1, board[0] // 2)
    return answer
