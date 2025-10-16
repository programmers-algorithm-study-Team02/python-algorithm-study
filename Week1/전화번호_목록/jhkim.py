"""
    어?? 이것도 풀었던 거 같은데?
    문자열 그대로 사전 순 정렬을 하면 쉽게 풀수 있는 문제
    정렬로 풀었으니 해시로 풀어보자
    dict로 하면 안에 뭘 넣어야 될지 모르겠으니까 set을 쓰자
    정렬로 풀면 케이스17: 8.17, 케이스18: 10.47
    해시로 풀면 케이스17: 6.15, 케이스18: 5.42
"""

def solution(phone_book):
    factors = set(phone_book)
    
    for num in phone_book:
        for idx in range(len(num)):
            prefix = num[:idx]
            if prefix in factors:
                return False
    return True
    
    