import sys
# input.txt 파일은 현재 파이썬 파일과 같은 경로에 위치
sys.stdin = open("input.txt","r")
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제>
# : 1920 _ 수 찾기
# https://www.acmicpc.net/problem/1920
# <등급>
# : 실버 4
    
# <내가 파악한 요구사항>
# : 완전 탐색

# <실제 요구사항>
# : 자료구조, 정렬, 이분 탐색, 해시를 사용한 집합과 맵
    
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <수도코드>
'''
n을 입력 받음.
n개의 수를 입력 받음
m을 입력 받음
m개의 수를 입력 받음
n개의 수들을 탐색하면서
만약 m[0~m]까지의 수가 있다면
1을 반환, 없다면 0을 반환
'''
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제풀이>
n = int(input())
list_n = list(map(int, input().split()))
m = int(input())
list_m = list(map(int, input().split()))

for i in list_n:
    for j in list_m:
        if list_n[i] == list_m[i]:
            print(1)
    

# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <정답 및 다른풀이>
'''
풀이 방법 1: 이진 탐색(Binary Search)
	1.	배열 A를 정렬합니다.
	2.	배열 B의 각 원소를 이진 탐색으로 배열 A에서 찾습니다.
	3.	이진 탐색은 **O(log N)**의 시간 복잡도를 가지므로, 전체 탐색은 **O((N + M) log N)**의 복잡도를 가집니다.
'''
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

n = int(input())
a = sorted(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

for num in b:
    print(binary_search(a, num))



'''
풀이 방법 2: 집합(Set)을 이용한 탐색
	1.	배열 A를 집합(set)으로 변환합니다.
	2.	배열 B의 각 원소를 집합에서 찾습니다.
	3.	집합의 탐색 시간 복잡도는 평균적으로 **O(1)**이므로, 전체 탐색은 **O(N + M)**입니다.
'''
n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

for num in b:
    print(1 if num in a else 0)


# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제를 통한 학습 내용>

# 이진 탐색 -> 정렬해야함
def binary_search(arr, target):
    left, right = 0, len(arr)-1
    
    while left <= right:
        mid = (left + right)//2
        
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return 0