def solution(cards1, cards2, goal):
    answer = "Yes"
    for i in goal:
        if cards1 and i == cards1[0]:
            cards1.pop(0)
        # i번 단어가 1번 배열안에 있으면 꺼냄
        elif cards2 and i == cards2[0]:
            cards2.pop(0)
        # i번 단어가 2번 배열안에 있으면 꺼냄
        else:
            answer = "No"
        # 없다면 "No"
    return answer

# 시간 복잡도 O(n)

# 시간 복잡도 O(1)로 하는 방법

from collections import deque

def solution2(cards1, cards2, goal):
    cards1, cards2 = deque(cards1), deque(cards2)
    for word in goal:
        if cards1 and word == cards1[0]:
            cards1.popleft()
        elif cards2 and word == cards2[0]:
            cards2.popleft()
        else:
            answer = "No"
    return answer