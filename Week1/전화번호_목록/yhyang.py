def solution(phone_book):
    phone_map = {}

    for number in phone_book:
        phone_map[number] = True

    for number in phone_book:
        prefix = ""
        for i in range(len(number) - 1):
            prefix += number[i]
            if prefix in phone_map:
                return False

    return True