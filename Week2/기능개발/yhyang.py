# 각 기능은 개발 속도가 다르고, 앞의 기능이 배포될 때 같이 배포되어야 한다.
# 각 기능의 개발 속도(speeds)와 현재 진행도(progresses)가 주어질 때, 각 배포마다 몇 개의 기능이 함께 배포되는지를 구하는 문제

def solution(progresses, speeds):
    answer = []
    days = []
    # answer은 각 배포 때 몇 개의 기능이 배포되는지 저장
    # days는 완성되는데 걸리는 일 수

    for i in range(len(progresses)):
        remain = 100 - progresses[i]
        day = (remain + speeds[i] - 1) // speeds[i]
        days.append(day)
    #  ramain = 100 - progresses[i] 남은 작업량 계산
    # (remain + speeds[i] - 1) // speeds[i] 올림 나눗셈으로 남은 날짜를 계산 2.1 일이 소요된다면 3일째에 완료됨
    current = days[0] # 현재 배포 기준일
    count = 1 # 현재 배포 묶음에 포함된 기능 갯수

    for i in range(1, len(days)):
        if days[i] <= current: # 현재 기능이 이전 기능보다 일찍 끝나거나 같은 날 끝남 -> 같이 배포 가능
            count += 1
        else: # 이전 기능보다 늦게 끝남 -> 새로운 배포 시작
            answer.append(count)
            count = 1
            current = days[i]

    answer.append(count) # 마지막 배포 추가
    return answer

# 시간복잡도 O(n)

