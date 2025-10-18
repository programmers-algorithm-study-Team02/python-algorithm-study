def solution(keyinput, board):
    location = [0, 0]

    maxWidth, maxHeight = board[0] // 2, board[1] // 2
    
    for key in keyinput:
        if key == "right":
             if location[0] + 1 <= maxWidth:
                location[0] += 1
        elif key == "left":
            if location[0] - 1 >= -maxWidth:
                location[0] -= 1
        elif key == "up":
            if location[1] + 1 <= maxHeight:
                location[1] += 1
        elif key == "down":
            if location[1] - 1 >= -maxHeight:
                location[1] -= 1    
                
    return location


# dictionary 활용 ver.

# def solution(keyinput, board):
#     location = [0, 0]

#     maxWidth, maxHeight = board[0] // 2, board[1] // 2
    
#     move = {
#         "up": (0, 1),
#         "down": (0, -1),
#         "left": (-1, 0),
#         "right": (1, 0)
#     }
    
#     for key in keyinput:
#         dx, dy = move[key]
#         new_x = location[0] + dx
#         new_y = location[1] + dy
        
#         if -maxWidth <= new_x <= maxWidth and -maxHeight <= new_y <= maxHeight:
#             location = [new_x, new_y]
                
#     return location