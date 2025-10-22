def solution(s):
    answer = 0
    s = list(s)
    
    for _ in range(len(s)):
        stack = []
        
        for i in range(len(s)):
            if len(stack) > 0:
                if stack[-1] == '[' and s[i] == ']': stack.pop()
                elif stack[-1] == '{' and s[i] == '}': stack.pop()
                elif stack[-1] == '(' and s[i] == ')': stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
                
        if len(stack) == 0:
            answer += 1
        
        s.append(s.pop(0))
    
    return answer


# deque 사용 ver.

# from collections import deque

# def solution(s):
#     answer = 0
#     s = deque(s)  # 리스트 대신 deque 사용 → 회전 O(1)
    
#     for _ in range(len(s)):
#         stack = []
        
#         for ch in s:
#             if stack and ((stack[-1] == '(' and ch == ')') or
#                           (stack[-1] == '[' and ch == ']') or
#                           (stack[-1] == '{' and ch == '}')):
#                 stack.pop()
#             else:
#                 stack.append(ch)
        
#         if not stack:  # 올바른 괄호 문자열이면
#             answer += 1
        
#         ch = s.popleft()  # 맨 왼쪽 요소를 꺼냄 → O(1)
# 		s.append(ch)      # 맨 뒤로 붙임 → O(1)
#         # s.rotate(-1)  # 왼쪽으로 1칸 회전 O(1)
    
#     return answer
