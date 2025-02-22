def solution(s):
    len_s = len(s)
    if len_s % 2 == 0:  # 짝수 길이
        return s[(len_s // 2) - 1: (len_s // 2) + 1]
    else:  # 홀수 길이
        return s[len_s // 2]
                   