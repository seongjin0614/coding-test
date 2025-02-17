def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command  # 리스트의 언패킹 활용
        after_array = sorted(array[i-1:j])  # 슬라이싱 후 정렬
        answer.append(after_array[k-1])  # k번째 수는 1-based index이므로 -1 필요

    return answer