def solution(keyinput, board):
    answer = [0, 0]
    
    max_x = board[0] // 2
    max_y = board[1] // 2
    
    for key in keyinput:
        next_point = move(key, answer)
        if abs(next_point[0]) <= max_x and abs(next_point[1]) <= max_y:
            answer = next_point
        
    
    return answer

def move(key, point):
    keymap = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}
    return [point[0] + keymap[key][0], point[1] + keymap[key][1]]
