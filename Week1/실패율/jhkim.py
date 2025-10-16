"""
    실패율: 채류 플레이어의 수/ 도달 플레이어 수(클리어 + 채류)
    input: 사용자가 채류 중인 스테이지 번호 배열
    output: 실패율이 높은 수부터 내림차순 정렬 배열, 이외에는 사전 순 정렬
"""

def solution(N, stages):
    s_players = {i: 0 for i in range(1, N + 1)} # stay
    de_player = len(stages) # denominator
    f_rates = [] # failure rates
    
    # 각 stage 채류 플레이어 수 저장
    for stage in stages:
        if stage <= N:
            s_players[stage] += 1
            
    # 실패율 계산: stage 1 ~ stage N
    for stage in range(1, N + 1):
        stay = s_players[stage]
        # python2에서는 정수 연산이 되어 // 처럼 몫만 남음
        rate = stay / de_player if de_player else 0
        f_rates.append((stage, rate))
        # print(f"rate: {rate}")
        de_player -= stay
        
    # 정렬: 1. rate 내림, 2. stage 오름
    f_rates.sort(key=lambda x: (-x[1], x[0]))
    return [stage for stage, _ in f_rates]