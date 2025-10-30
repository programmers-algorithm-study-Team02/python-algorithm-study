def solution(n, computers):
    answer = 0

    def visit_network(src):
        visit.add(src)
        for dst, connected in enumerate(computers[src]):
            if connected and dst not in visit:
                visit_network(dst)
    
    visit = set()
    for computer in range(n):
        if computer not in visit:
            answer += 1
            visit_network(computer)
            
    return answer
    
