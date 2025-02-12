
student = list(map(int, input().split()))
k = int(input())

n = len(student)

answer = 0

for i in range(n):
  if student[i] >= k:
    answer += 1
    
    
print(answer)
