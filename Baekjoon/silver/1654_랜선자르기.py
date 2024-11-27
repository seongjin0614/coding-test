import sys
# input.txt 파일은 현재 파이썬 파일과 같은 경로에 위치
sys.stdin = open("input.txt","r")
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제>
# : 1654 _ 랜선 자르기
# https://www.acmicpc.net/problem/1654
# <등급>
# : 실버2
    
# <내가 파악한 요구사항>
# : 

# <실제 요구사항>
# : 이분 탐색, 매개 변수 탐색
    
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <수도코드>
'''
k(현재 가지고 있는 랜선 개수), n(필요한 랜선 개수) 을 입력 받음
k만큼 반복으로 각 랜선의 길이를 입력 받은 후 리스트로 저장


'''
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제풀이>

# 입력
k, n = map(int, input().split())
cables = [ (int(input())) for _ in range(k) ]

# 특정 길이 x로 랜선을 잘라 만들 수 있는 개수 계산
def count_pieces(cables, length):
    return sum(cable // length for cable in cables)

def binary_search(cables, n):
    left, right = 1, min(cables)
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        if count_pieces(cables, mid) >= n:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return result

print(binary_search(cables, n))



# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <정답 및 다른풀이>
k,n = map(int, input().split())
cables = [ (int(input())) for _ in range(k) ]

def count_pieces(cables, length):
    return sum(cable // length for cable in cables)

def binary_search(cables, n):
    left, right = 1, max(cables)
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        if count_pieces(cables, mid) >= n:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return result

print(binary_search(cables, n))

# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제를 통한 학습 내용>

1. 기본 이진 탐색(특정 값 찾기)

def binary_search(array, target):
    left, right = 0, len(array)-1
    
    while left <= right:
        mid = (left + right) // 2
        
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1


2. 범위를 이용한 이진 탐색(조건 만족 탐색)

def binary_search_range(left, right, is_valid):
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if is_valid(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return result

def is_valid(mid):
    return (mid //2) >= 5
