def solution(progresses, speeds):
    answer = []
    days = []

    for i in range(len(progresses)):
        remain = 100 - progresses[i]
        day = (remain + speeds[i] - 1) // speeds[i]
        days.append(day)

    current = days[0]
    count = 1

    for i in range(1, len(days)):
        if days[i] <= current:
            count += 1
        else:
            answer.append(count)
            count = 1
            current = days[i]

    answer.append(count)
    return answer

