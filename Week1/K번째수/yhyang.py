def solution(array, commands):
    answer = []
    for a, b, c in commands:
            num_list = sorted(array[a-1:b])
            answer.append(num_list[c-1])
    return answer