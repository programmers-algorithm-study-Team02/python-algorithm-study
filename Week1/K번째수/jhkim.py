"""
    slicing 'i' to 'j' 
    'k'th factor
    이거 람다랑 컴프리헨션 쓰면 한줄로도 될 것같은데?
"""
def solution(array, commands):
    answer = []
    
    for cmd in commands:
        temp = array[cmd[0] - 1:cmd[1]]
        temp.sort()
        answer.append(temp[cmd[2] - 1])
    
    return answer