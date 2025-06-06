import sys
# input.txt 파일은 현재 파이썬 파일과 같은 경로에 위치
sys.stdin = open("input.txt","r")
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제>
# :

# <등급>
# :
    
# <내가 파악한 요구사항>
# :

# <실제 요구사항>
# :
    
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <수도코드>

# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제풀이>

# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <정답 및 다른풀이>
n, m = map(int, input().split())
result = []

def backtrack(start):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    for i in range(start, n + 1):
        if i not in result:
            result.append(i)
            backtrack(i + 1)
            result.pop()

backtrack(1)
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제를 통한 학습 내용>