nums = list(map(int, input().split()))
n = len(nums)
count = 0
max_count = 0
for i in range(n):
  if nums[i] == 1:
    count += 1
    max_count = max(max_count, count)
  else:
    count = 0
    
print(max_count)