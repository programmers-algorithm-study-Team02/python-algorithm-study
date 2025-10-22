def solution(progresses, speeds):
    days = []
    
    # 작업 기간 계산
    for i in range(len(progresses)):
        remain = 100 - progresses[i]
        # day = math.ceil(remain / speeds[i]) -> 문제 코드
        day = (remain + speeds[i] - 1) // speeds[i] # -> 해결
        
        days.append(day)
            
    # 배포 순서 확인
    res = []
    max_day = days[0]
    cnt = 1
    
    for i in range(1, len(days)) :        
        if days[i] <= max_day:
            cnt += 1
        else:
            res.append(cnt)
            cnt = 1
            max_day = days[i]
            
    res.append(cnt)
    return res