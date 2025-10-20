from collections import deque

def solution(s):
    answer = 0
    
    brackets = deque(s)
    for i in range(len(s)):
        if check_bracket(brackets):
            answer += 1
        brackets.rotate()
    
    return answer

def check_bracket(brackets):
    stack = []
    for bracket in brackets:
        if len(stack) > 0 and match_bracket((stack[-1], bracket)):
            stack.pop()
        else:
            stack.append(bracket)
            
    if len(stack) == 0:
        return True
    return False
            
def match_bracket(bracket):
    if ((bracket[0] == "(" and bracket[1] == ")") or
        (bracket[0] == "{" and bracket[1] == "}") or
        (bracket[0] == "[" and bracket[1] == "]")):
        return True
    return False
