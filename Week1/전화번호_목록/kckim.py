def solution(phone_book):
    answer = True
    
    phone_book.sort()
    
    prev_phone = "tmp"
    for phone in phone_book:
        if phone.startswith(prev_phone):
            return False
        prev_phone = phone
    
    return answer
