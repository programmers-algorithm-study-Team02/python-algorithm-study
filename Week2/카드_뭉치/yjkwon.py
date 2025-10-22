def solution(cards1, cards2, goal):
    
    for word in goal:
		# cards1이 비어있지 않고, 첫 번째 원소가 word인지 확인(빈 배열일 경우를 제외하기 위함)
        if cards1 and cards1[0] == word:
            cards1.pop(0)
        elif cards2 and cards2[0] == word:
            cards2.pop(0)
        else:
            return "No"
    
    return "Yes"


# 포인터 이동 방식

# def solution(cards1, cards2, goal):
    
#     for word in goal:
# 		    # cards1이 비어있지 않고, 첫 번째 원소가 word인지 확인(빈 배열일 경우를 제외하기 위함)
#         if cards1 and cards1[0] == word:
#             cards1.pop(0)
#         elif cards2 and cards2[0] == word:
#             cards2.pop(0)
#         else:
#             return "No"
    
#     return "Yes"