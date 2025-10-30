def solution(maps):
    answer = []
    visit = set()
    
    def valid_pos(pos):
        i, j = pos
        if not (0 <= i < len(maps) and 0 <= j < len(maps[0])):
            return False
        return True
    
    def get_food(pos):
        food = 0
        stack = [pos]
        while stack:
            i, j = stack.pop()
            food += (int)(maps[i][j])
            
            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                new_pos = (i + di, j + dj)
                if valid_pos(new_pos) and new_pos not in visit:
                    if maps[new_pos[0]][new_pos[1]] != 'X':
                        visit.add(new_pos)
                        stack.append(new_pos)
        return food
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            pos = (i, j)
            if maps[i][j] != 'X' and pos not in visit:
                visit.add((pos))
                answer.append(get_food(pos))
    
    if not answer:
        answer.append(-1)

    answer.sort()
    
    return answer
        
