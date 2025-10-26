import math

# 100 = progress + x*speed
def cal_day(progress, speed):
    return math.ceil((100 - progress) / speed)

def solution(progresses, speeds):
    answer = []
    days = []
    cnt = 0
    
    # 개발 완료일 계산
    for idx, prog in enumerate(progresses):
        days.append(cal_day(prog, speeds[idx]))
    
    # 배포일
    deploy_day = days[0]
    
    for day in days:
        # 배포일 전 기능 개발 완료
        if day <= deploy_day:
            cnt += 1
        else:
            answer.append(cnt) 
            cnt = 1
            deploy_day = day
    # 마지막 배포        
    answer.append(cnt)
    return answer