import sys
# input.txt 파일은 현재 파이썬 파일과 같은 경로에 위치
sys.stdin = open("input.txt","r")
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제>
# : 1463 _ 1로 만들기
# https://www.acmicpc.net/problem/1463
# <등급>
# : 실버 3

# <내가 파악한 요구사항>
# : 수학

# <실제 요구사항>
# : 다이나믹 프로그래밍

# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <수도코드>
'''
1. x%3 == 0 -> x/3
2. x%2 == 0 -> x/2
3. x - 1
연산의 최소 횟수

x를 입력 받음
x가 1일 될때까지 연산 반복 수행
연산이 한번 진행될 때마다 count +=1

'''
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제풀이>
'''
x = int(input())

count = 0

while x != 1:
    if x%3 == 0 and x//3 >= 1:
        x = x/3
        count += 1
    elif x%2 ==0 and x//2 >= 1:
        x = x/2
        count += 1
    else:
        x = x-1
        count += 1

print(count)
'''
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <정답 및 다른풀이>
def make_one(n):
    # DP 배열 생성
    dp = [0] * (n + 1)
    
    # DP 계산
    for i in range(2, n + 1):
        
        # 기본적으로 이전 숫자에서 1을 뺀 경우
        dp[i] = dp[i - 1] + 1
        
        # 2로 나누어 떨어지는 경우
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        
        # 3으로 나누어 떨어지는 경우
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    
    return dp[n]

# 입력
n = int(input())
print(make_one(n))
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제를 통한 학습 내용>