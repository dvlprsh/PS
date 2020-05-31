//Solve
def solution(phone_book):
    answer = True
    phone_book.sort(key=len)

    while phone_book:
        prefix = phone_book.pop(0)
        for phone in phone_book:
            if phone.startswith(prefix, 0) == True:
                return False


    return answer