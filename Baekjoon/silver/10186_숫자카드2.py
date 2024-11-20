import sys
# input.txt 파일은 현재 파이썬 파일과 같은 경로에 위치
sys.stdin = open("input.txt","r")
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제>
# : 10186 _ 숫자카드 2

# <등급>
# : 실버 4
    
# <내가 파악한 요구사항>
# : 브루트 포스

# <실제 요구사항>
# : 이분 탐색, 해시를 사용한 집합과 맵, 정렬, 자료 구조
    
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <수도코드>
'''
n(숫자카드의개수) 입력 받음
숫자카드의 적혀있는 정수 입력 받음
셋째 줄에는 m(주어진 정수의 개수) 입력 받음
구해야 할 정수 입력 받음
m개의 주어진 정수를 n개의 숫자카드에서 몇개를 가지고 있는지 파악
출력
'''
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제풀이>
n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

result = []

for i in range(m):
    count = 0
    for j in range(n):
        if m_list[i] == n_list[j]:
            count += 1
    result.append(count)

print(*result)
#  -->> 시간 초과


# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <정답 및 다른풀이>

# 딕셔너리 방법
from collections import Counter

# 입력
N = int(input())
cards = list(map(int, input().split()))
M = int(input())
queries = list(map(int, input().split()))

# 숫자 카드 등장 횟수 카운팅
card_count = Counter(cards)

# 결과 출력
result = [card_count[query] for query in queries]
print(*result)

# -----------------------------------------------------------------

# 이진 탐색 방법
from bisect import bisect_left, bisect_right

# 입력
N = int(input())
cards = sorted(map(int, input().split()))  # 정렬된 카드 배열
M = int(input())
queries = list(map(int, input().split()))

# 특정 숫자의 개수를 구하는 함수
def count_occurrences(arr, x):
    left = bisect_left(arr, x)
    right = bisect_right(arr, x)
    return right - left

# 결과 출력
result = [count_occurrences(cards, query) for query in queries]
print(*result)
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제를 통한 학습 내용>
'''
문제의 범위를 확인하고 시간복잡도를 고려해 코드를 구현할것
'''