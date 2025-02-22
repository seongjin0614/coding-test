def solution(phone_number):
    len_phone_number = len(phone_number)
    phone_number = list(phone_number)
    for i in range(len_phone_number-4):
        phone_number[i] = "*"
    return ''.join(phone_number)