"""
 수포자1: 1-5 반복
 수포자2: 21232425 반복
 수포자3: 3311224455 반복
"""
SUPO_PATTERN = {
    '1': [1, 2, 3, 4, 5],
    '2': [2, 1, 2, 3, 2, 4, 2, 5],
    '3': [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
}

def solution(answers):
    scores = [0, 0, 0]
    for idx in range(len(answers)):
        ans = answers[idx]
        if ans == SUPO_PATTERN['1'][idx % len(SUPO_PATTERN['1'])]:
            scores[0] += 1
        if ans == SUPO_PATTERN['2'][idx % len(SUPO_PATTERN['2'])]:
            scores[1] += 1
        if ans == SUPO_PATTERN['3'][idx % len(SUPO_PATTERN['3'])]:
            scores[2] += 1
    max_score = max(scores)
    result = []
    
    for idx, score in enumerate(scores):
        if score == max_score:
            result.append(idx + 1)
            
    return result

