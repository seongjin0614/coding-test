import sys
from collections import Counter

input = sys.stdin.readline

n, m = map(int, input().split())

words = []

# 단어 필터링: 길이가 m 이상인 것만 수집
for _ in range(n):
    word = input().strip()
    if len(word) >= m:
        words.append(word)

# 단어 등장 횟수 집계
counter = Counter(words)

# 정렬: 
# 1) 자주 나오는 단어 순 (내림차순)
# 2) 단어 길이 긴 순 (내림차순)
# 3) 알파벳 역순 (사전 내림차순)
sorted_words = sorted(counter.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

# 출력
for word, _ in sorted_words:
    print(word)
