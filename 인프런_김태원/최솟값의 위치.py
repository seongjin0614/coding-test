# 제한사항:
# 입력값 범위: 3 <= n <= 100,000
# 시간복잡도: O(n), O(nlogn)을 넘지 않는다.

# 입력값으로 배열을 입력받음
# 배열의 원소를 순차적으로 순회함
# 기본값을 설정하고 기본값보다 작다면 값을 변경함

data = list(map(int, input().split()))

min = float('inf')
answer = -1
n = len(data)

for i in range(n):
  if data[i] < min:
    min = data[i]
    answer = i
    
print(answer)