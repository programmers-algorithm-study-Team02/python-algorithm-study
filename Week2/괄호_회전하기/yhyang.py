def solution(s):
    answer = 0
    pairs = {')': '(', ']': '[', '}': '{'}

    for x in range(len(s)):
        rotated = s[x:] + s[:x]
        stack = []
        correct = True

        for ch in rotated:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack or stack[-1] != pairs[ch]:
                    correct = False
                    break
                stack.pop()
        if correct and not stack:
            answer += 1

    return answer