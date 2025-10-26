from collections import deque

def solution(cards1, cards2, goal):
    goal = deque(goal)
    cp1 = 0
    cp2 = 0
    
    while goal:
        word = goal[0]
        if cp1 < len(cards1) and word == cards1[cp1]:
            cp1 += 1
            goal.popleft()
        
        elif cp2 < len(cards2) and word == cards2[cp2]:
            cp2 += 1
            goal.popleft()
        
        else:
            return "No"
        
    return "Yes"