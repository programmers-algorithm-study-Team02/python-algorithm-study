def solution(answers):
    count = [0, 0, 0]
    
    solves = [[],[],[]]
    solves[0] = [1, 2, 3, 4, 5]
    solves[1] = [2, 1, 2, 3, 2, 4, 2, 5]
    solves[2] = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(3):
        for aIndex in range(len(answers)):
            solve = solves[i]
            if solve[aIndex % len(solve)] == answers[aIndex]:
                count[i] += 1
            
    answer = list()
    
    for i in range(3):
        if max(count) == count[i]:
            answer.append(i + 1)
            
    
    return answer
