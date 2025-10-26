def solution(s):
    answer = 0 # 올바른 괄호 문자열 개수를 셀 변수
    pairs = {')': '(', ']': '[', '}': '{'}  # 닫는 괄호가 Key, 그에 대응하는 여는 괄호를 값으로 저장

    for x in range(len(s)):
        rotated = s[x:] + s[:x] # 문자열을 x칸 만큼 회전
        stack = [] # 여는 괄호를 저장
        correct = True # 회전된 문자열이 올바른 괄호인지 표시

        for ch in rotated:
            if ch in "([{": # 여는 괄호라면 스텍에 추가
                stack.append(ch)
            else:
                if not stack or stack[-1] != pairs[ch]: # 스텍이 비어있지 않은가, 스텍이 마지막 값이 해당 괄호의 닫는 값인가 확인
                    correct = False
                    break # 둘다 아니라면 False
                stack.pop()
        if correct and not stack:
            answer += 1 # 모든 검사 후에 스텍이 비어있다면 정상적인 괄호

    return answer

# 시간 복잡도 O(n2)