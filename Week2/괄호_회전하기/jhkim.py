"""
이건 괄호 닫기 문제 응용 버전인 것같네

input: 괄호 문자열 s
func: 0~len(s)만큼 괄호 회전
output: 올바른 괄호 문자열이 되는 경우의 수

회전이란? -> 문자열 shift 하는 것
10^6? 그냥 브루트포스로 될 것같은데?
"""

def push(s, x):
    temp = []
    temp.append(s[x:])
    temp.append(s[:x])
    return "".join(temp)

def check_bracket(s):
    pattern = {"(": ")", "{": "}", "[": "]"}
    stack = []
     
    for idx, bracket in enumerate(s):
        if len(stack) > 0 and stack[-1] in pattern.keys():
            if pattern[stack[-1]] == bracket:
              # print(f"meet {bracket}")
              stack.pop()
            else:
                stack.append(bracket)
        else:
            # print(f"stack in {bracket}")
            stack.append(bracket)
        # print(stack)
    return False if len(stack) != 0 else True

def solution(s):
    answer = -1
    cnt = 0
    
    for idx in range(len(s)):
        cur_str = push(s, idx)
        if check_bracket(cur_str):
            # print(f"{cur_str} is collect!")
            cnt += 1
    
    return cnt