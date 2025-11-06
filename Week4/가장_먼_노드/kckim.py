from collections import deque, defaultdict

def solution(n, edges):
    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    visit = {1}
    depth, count = 0, 0
    bfs = deque([(1, 1)])
    while bfs:
        index, d = bfs.popleft()
        
        if d > depth:
            depth = d
            count = 0
            
        count += 1
            
        for v in graph[index]:
            if v not in visit:
                visit.add(v)
                bfs.append((v, d + 1))
    
    return count
