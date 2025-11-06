def solution(k, dungeons):
    answer = 0
    
    def explore(point, index, visit):
        result = len(visit)
        for i in range(len(dungeons)):
            min_point, use_point = dungeons[i]
            if i not in visit and point >= min_point:
                visit.add(i)
                point -= use_point
                result = max(result, explore(point, i, visit))
                point += use_point
                visit.remove(i)
        return result
    
    for i in range(len(dungeons)):
        min_point, use_point = dungeons[i]
        if k >= min_point:
            answer = max(answer, explore(k - use_point, i, {i}))
    
    return answer
