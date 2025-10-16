"""
    그냥 구현문제 같네
    케이스8 실패 - ???
        - ["up", "up", "up", "down"] [3, 3] -> 기대: [0, 0], 실제: [0, 1]
        - 범위를 넘은 상태에서의 입력은 무시되어야함
    match 지원x
"""
def solution(keyinput, board):
    cur_location = [0, 0]
    
    for cmd in keyinput:
        if cmd == "up":
            if cur_location[1] < (board[1] // 2):
                cur_location[1] += 1
        elif cmd == "down":
            if cur_location[1] > -(board[1] // 2):
                cur_location[1] -= 1
        elif cmd == "right":
            if cur_location[0] < (board[0] // 2):
                cur_location[0] += 1
        elif cmd == "left":
            if cur_location[0] > -(board[0] // 2):
                cur_location[0] -= 1
                
    return cur_location