def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False
    return True


## 해시 활용 ver.

# def solution(phone_book):
#     hash_map = {}
    
#     for nums in phone_book:
#         hash_map[nums] = 1
        
#     for nums in phone_book:
#         arr = ""
        
#         for num in nums:
#             arr += num
            
#             if arr in hash_map and arr != nums:
#                 return False
#     return True