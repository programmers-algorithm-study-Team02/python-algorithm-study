def solution(commands):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    x, y, direction = 0, 0, 0
    
    for command in commands:
        if command == 'R':
            direction = (direction + 1) % 4
        elif command == 'L':
            direction = 3 if direction == 0 else direction - 1
        elif command == 'G':
            x += dx[direction]
            y += dy[direction]
        elif command == 'B':
            x -= dx[direction]
            y -= dy[direction]
    
    return [x, y]
