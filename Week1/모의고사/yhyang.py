def solution(answers):
    answer = []
    mogo = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    index = [0, 0, 0]
    score = [0, 0, 0]

    for i in range(len(answers)):
        for j in range(len(mogo)):
            if answers[i] == mogo[j][index[j]]:
                score[j] += 1

            index[j] += 1

            if index[j] >= len(mogo[j]):
                index[j] = 0;

    max_score = max(score)

    for k in range(len(score)):
        if max_score == score[k]:
            answer.append(k + 1)

    return answer