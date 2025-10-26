# 주어진 각 시점의 주식 가격이 얼마 동안 떨지지 않았는지 구하는 문제

def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []

# n은 주가 의 갯수, answer은 각 시점별 결과 저장 리스트, stack은 주가가 떨어지지 않은 인덱스 들을 저장하는 스텍

    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]:
            idx = stack.pop()
            # 주가가 떨어진 시점의 인덱스를 꺼냄
            answer[idx] = i - idx
            # 가격이 유지된 시간을 기록
        stack.append(i)
    while stack:
        idx = stack.pop()
        answer[idx] = n - 1 - idx
        # 가격이 끝까지 유지된 시간을 처리

    return answer

