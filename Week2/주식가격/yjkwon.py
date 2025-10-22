def solution(prices):
    answer = [0] * len(prices)
    
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            # 가격이 떨어지지 않았으면 지속 시간 +1
            answer[i] += 1
            
            # 가격이 떨어지는 순간 중단
            if prices[i] > prices[j]:
                break
    
    return answer


# 스택 활용

# def solution(prices):
#     answer = [0] * len(prices)
#     stack = []   # 초(sec), 즉 인덱스를 저장
    
#     for i in range(len(prices)):
#         # 현재 가격이 이전보다 작으면 스택에서 꺼냄 + 시간(인덱스) 계산
#         while stack and prices[i] < prices[stack[-1]]:
#             j = stack.pop()
#             answer[j] = i - j
#         stack.append(i)
    
#     # 남은 인덱스들 -> 끝까지 가격이 떨어지지 않은 시점들
#     for j in stack:
#         answer[j] = len(prices) - 1 - j
    
#     return answer