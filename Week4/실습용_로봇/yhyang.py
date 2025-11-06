def solution(command):
    dire = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x = y = 0
    dir_idx = 0

    for c in command:
        if c == "R":
            dir_idx = (dir_idx + 1) % 4
        elif c == "L":
            dir_idx = (dir_idx - 1) % 4
        elif c == "G":
            dx, dy = dire[dir_idx]
            x += dx
            y += dy
        elif c == "B":
            dx, dy = dire[dir_idx]
            x -= dx
            y -= dy

    return [x, y]