def solution(prices):
    answer = [0] * len(prices)
    bucket = [0]

    for ref_idx in range (1, len(prices)):
        # bucket.top 시점의 가격이 기준시점의 가격보다 높은 경우 -> 가격 하락
        while bucket and prices[bucket[-1]] > prices[ref_idx]:
            falling_idx = bucket.pop()
            # 유지 시간 계산
            answer[falling_idx] = ref_idx - falling_idx
        bucket.append(ref_idx) # 갱신
    
    # 가격이 떨어지지않은 경우 처리
    while bucket:
        not_falling_idx = bucket.pop()
        answer[not_falling_idx] = len(prices) - not_falling_idx - 1
        
    return answer

"""
list version
    딱히 결과가 나쁘다곤 생각하지 않았는데 stack을 이용한 버전과 비교하면 
    확실히 성능이 나쁜 듯

    정확성  테스트
    테스트 1 〉	통과 (0.01ms, 9.21MB)
    테스트 2 〉	통과 (0.05ms, 9.3MB)
    테스트 3 〉	통과 (0.57ms, 9.29MB)
    테스트 4 〉	통과 (1.11ms, 9.2MB)
    테스트 5 〉	통과 (1.33ms, 9.34MB)
    테스트 6 〉	통과 (0.02ms, 9.14MB)
    테스트 7 〉	통과 (0.35ms, 9.24MB)
    테스트 8 〉	통과 (0.42ms, 9.31MB)
    테스트 9 〉	통과 (0.06ms, 9.24MB)
    테스트 10 〉 통과 (1.00ms, 9.21MB)
    
    효율성  테스트
    테스트 1 〉	통과 (99.30ms, 18MB)
    테스트 2 〉	통과 (86.08ms, 16.5MB)
    테스트 3 〉	통과 (123.31ms, 18.9MB)
    테스트 4 〉	통과 (89.03ms, 17.1MB)
    테스트 5 〉	통과 (64.53ms, 16.1MB)
"""

"""
queue version
    로직 상 list version과 같은 이중 루프인데 결과에 차이가 남
    이거는 pop()과 popleft()의 성능 차이 일듯함

    정확성  테스트
    테스트 1 〉	통과 (0.00ms, 9.06MB)
    테스트 2 〉	통과 (0.03ms, 9.25MB)
    테스트 3 〉	통과 (0.28ms, 9.34MB)
    테스트 4 〉	통과 (0.30ms, 9.27MB)
    테스트 5 〉	통과 (0.39ms, 9.18MB)
    테스트 6 〉	통과 (0.01ms, 9.19MB)
    테스트 7 〉	통과 (0.18ms, 9.25MB)
    테스트 8 〉	통과 (0.21ms, 9.34MB)
    테스트 9 〉	통과 (0.02ms, 9.26MB)
    테스트 10 〉 통과 (0.38ms, 9.16MB)
    
    효율성  테스트
    테스트 1 〉	통과 (55.13ms, 17.8MB)
    테스트 2 〉	통과 (42.93ms, 16.7MB)
    테스트 3 〉	통과 (71.06ms, 18.5MB)
    테스트 4 〉	통과 (54.62ms, 17.3MB)
    테스트 5 〉	통과 (35.05ms, 15.9MB)
"""

"""
stack version
    여기서 더 간단하고 직관적으로 만들 방법이 있을 것같은 느낌이 드는데 
    더 이상 생각이 안난다...

    정확성  테스트
    테스트 1 〉	통과 (0.01ms, 9.26MB)
    테스트 2 〉	통과 (0.03ms, 9.16MB)
    테스트 3 〉	통과 (0.40ms, 9.34MB)
    테스트 4 〉	통과 (0.24ms, 9.34MB)
    테스트 5 〉	통과 (0.28ms, 9.45MB)
    테스트 6 〉	통과 (0.02ms, 9.16MB)
    테스트 7 〉	통과 (0.17ms, 9.3MB)
    테스트 8 〉	통과 (0.18ms, 9.3MB)
    테스트 9 〉	통과 (0.02ms, 9.28MB)
    테스트 10 〉 통과 (0.28ms, 9.29MB)
    
    효율성  테스트
    테스트 1 〉	통과 (23.49ms, 18.1MB)
    테스트 2 〉	통과 (17.21ms, 16.6MB)
    테스트 3 〉	통과 (25.87ms, 19MB)
    테스트 4 〉	통과 (21.09ms, 17.3MB)
    테스트 5 〉	통과 (15.31ms, 16MB)
"""