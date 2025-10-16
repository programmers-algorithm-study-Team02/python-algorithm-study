from collections import Counter

def solution(N, stages):
    answer = []

    fail_count = Counter(stages)
    failure = {}
    num_people = len(stages)
    
    for stage in range(1, N + 1):
        if num_people == 0:
            failure[stage] = 0
            continue
        failure[stage] = float(fail_count[stage]) / float(num_people)
        num_people -= fail_count[stage]
    
    answer = sorted(failure, key=lambda x: (-failure[x], x))
    
    return answer
