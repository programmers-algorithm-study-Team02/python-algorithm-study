import math

def solution(progresses, speeds):
    answer = []
    
    num_progresses = len(progresses)
    
    prod_day = 0
    for i in range(num_progresses):
        progress, speed = progresses[i], speeds[i]
        day = math.ceil(float(100 - progress) / float(speed))
        
        if prod_day < day:
            answer.append(1)
            prod_day = day
        else:
            answer[len(answer) - 1] += 1
    
    return answer
