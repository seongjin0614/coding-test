def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    
    length = len(A)
    
    count = 0
    
    for i in range(length):
        C = A[i] * B[i]
        count += C

    return count