def solution(numbers):
    answer = []
    
    len_numbers = len(numbers)
    
    for i in range(len_numbers):
        for j in range(i+1,len_numbers):
            result = numbers[i]+numbers[j]
            answer.append(result)
            
    answer = set(answer)
    answer = list(answer)
    answer.sort()
    
    return answer