import sys
# input.txt 파일은 현재 파이썬 파일과 같은 경로에 위치
sys.stdin = open("input.txt","r")
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제>
# : 1927_최소힙

# <등급>
# : 실버 2
    
# <내가 파악한 요구사항>
# :

# <실제 요구사항>
# : 우선순위 큐
    
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <수도코드>
# 연산의 개수 n을 입력 받음
# n개의 개수만큼 정수 x를 입력 받음
# x가 자연수이면 배열에 x를 추가
# x가 0이면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제풀이>
import sys
import heapq

n = int(sys.stdin.readline())  # 입력 최적화
heap = []  # 최소 힙

for _ in range(n):
    x = int(sys.stdin.readline())  # 빠른 입력 처리
    if x == 0:
        if heap:
            print(heapq.heappop(heap))  # 가장 작은 값 출력 후 제거
        else:
            print(0)  # 힙이 비어 있으면 0 출력
    else:
        heapq.heappush(heap, x)  # 최소 힙에 추가
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <정답 및 다른풀이>

# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제를 통한 학습 내용>