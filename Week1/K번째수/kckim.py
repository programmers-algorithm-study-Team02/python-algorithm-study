def solution(array, commands):
    answer = []
    
    for command in commands:
        answer.append(knum(array, command))
        
    return answer

def knum(array, command):
    subarray = array[command[0] - 1 : command[1]]
    subarray.sort()
    return subarray[command[2] - 1]
