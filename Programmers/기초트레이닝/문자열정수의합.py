def solution(num_str):
    answer = 0
    for i in num_str:
        number = int(i)
        answer += number
    return answer