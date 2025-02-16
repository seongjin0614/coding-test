def solution(arr):
    answer = []
    len_arr = len(arr)
    for i in range(len_arr):
        mul = arr[i]
        for j in range(mul):
            answer.append(mul)
    return answer