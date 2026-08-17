def solution(phone_book):
    phone_set = set(phone_book)

    for phone_number in phone_book:
        for num in range(1, len(phone_number)):
            if phone_number[:num] in phone_set:
                return False

    return True
