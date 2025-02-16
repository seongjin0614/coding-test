def solution(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        even = 0
        for i in range(1,n+1):
            if i % 2 == 0:
                even += i*i
        return even
    else:
        odd = 0
        for j in range(1, n+1):
            if j % 2 != 0:
              odd += j
        return odd