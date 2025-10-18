def solution(N, stages):
    result = []
    total = len(stages)
    
    for i in range(1, N + 1):
        playing = stages.count(i)
        # 삼항연산자. 스테이지1에 도달한 사람은 전체
        fail_rate = 0 if total == 0 else playing / total
        result.append((i, fail_rate))
        # 전체에서 이전단계 클리어 못한 플레이어 제외 = 다음 단계 도달한 사람
        total -= playing    

    # 실패율 기준 내림차순 정렬, 같으면 번호 오름차순
    result.sort(key=lambda x: (-x[1], x[0]))
    return [r[0] for r in result]