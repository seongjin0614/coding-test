def solution(numbers):
    original = {0,1,2,3,4,5,6,7,8,9}
    numbers = set(numbers)
    answer = original - numbers
    answer = sum(list(answer))
    return answer