import sys
# input.txt 파일은 현재 파이썬 파일과 같은 경로에 위치
sys.stdin = open("input.txt","r")
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제>
# : 16555_가운데를 말해요

# <등급>
# : 골드 2
    
# <내가 파악한 요구사항>
# :

# <실제 요구사항>
# :
    
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <수도코드>
# 리스트에 정수 삽입
# 정렬
# 리스트의 길이가 짝수 -> 배열의 길이 /2
# 리스트의 길이가 홀수 -> 배열의 길이 //2
# 출력

# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제풀이>

# 정수의 개수 n
# n = int(input())

# backjoon = []

# for i in range(n):
#   integer = int(input())
#   backjoon.append(integer)
#   backjoon.sort()
#   if len(backjoon) == 1:
#     print(backjoon[0])
#   elif len(backjoon) % 2 == 0:
#     print(backjoon[(len(backjoon) // 2)-1])
#   else:
#     print(backjoon[len(backjoon) // 2])
# --> 시간초과 발생

# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <정답 및 다른풀이>
import heapq
import sys

input = sys.stdin.readline
n = int(input())

max_heap = []  # 중간 이하 (음수)
min_heap = []  # 중간 초과

for _ in range(n):
    num = int(input())

    # 1. max_heap에 우선 추가
    heapq.heappush(max_heap, -num)

    # 2. max_heap > min_heap이면 값 교환
    if min_heap and -max_heap[0] > min_heap[0]:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))

    # 3. 크기 균형 맞추기
    if len(max_heap) > len(min_heap) + 1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    elif len(min_heap) > len(max_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))

    # 4. 중간값 출력
    print(-max_heap[0])
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제를 통한 학습 내용>