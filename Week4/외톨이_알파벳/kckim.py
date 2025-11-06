from collections import defaultdict

def solution(input_string):
    answer = ''
    
    exist = defaultdict(int)
    
    prev = "N"
    for c in input_string:
        if prev == c:
            continue
        prev = c
        
        exist[c] += 1

    alphabet = 'abcdefghijklmnopqrstuvwxyz' 
    for a in alphabet:
        if exist[a] > 1:
            answer += a
    
    if not answer:
        answer = 'N'
            
    return answer
