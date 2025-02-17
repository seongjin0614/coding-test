def solution(s):
    s = list(map(int, s.split()))
    min_s = min(s)
    max_s = max(s)
    answer = str(min_s) + " " +str(max_s)
    return answer