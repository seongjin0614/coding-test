import sys
# input.txt 파일은 현재 파이썬 파일과 같은 경로에 위치
sys.stdin = open("input.txt","r")
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제>
# : 1764_듣보잡

# <등급>
# : 실버 4
    
# <내가 파악한 요구사항>
# : 집합

# <실제 요구사항>
# : 문자열, 정렬, 해시를 사용한 집합과 맵

# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <수도코드>
# 듣의 수 N과 보의 수 M을 입력 받음
# 듣의 수 N만큼 입력받아 집합으로 저장
# 보의 수 M만큼 입력받아 집합으로 저장
# 듣과 보의 교집합을 구함
# 개수를 구함
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제풀이>
n,m = map(int, input().split())

n_set = set()
for _ in range(n):
  n_set.add(input())
  
m_set = set()
for _ in range(m):
  m_set.add(input())
  
intersection = n_set & m_set
intersection_len = len(intersection)

print(intersection_len)
for name in sorted(intersection):
  print(name)
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <정답 및 다른풀이>

# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제를 통한 학습 내용>
# ✅ N, M이 최대 500,000일 때, 시간 초과 없이 처리해야 함.
# ✅ 리스트(List)에서 in 연산을 사용하면 O(N) → 시간 초과 위험
# ✅ Set을 사용하면 평균적으로 O(1) 연산이 가능하므로 적합