def solution(arr, n):
    len_arr = len(arr)
    if len_arr % 2 == 0:
        for i in range(len_arr):
            if i % 2 != 0:
                arr[i] += n
    else:
        for i in range(len_arr):
            if i % 2 == 0:
                arr[i] += n
    answer = arr
    return answer