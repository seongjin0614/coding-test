def solution(array):
    answer = []
    len_array = len(array)
    max_num = 0
    max_index = 0
    for i in range(len_array):
        max_num = max(max_num, array[i])
        if max_num == array[i]:
            max_index = i
    answer.append(max_num)
    answer.append(max_index)
    
    
    return answer