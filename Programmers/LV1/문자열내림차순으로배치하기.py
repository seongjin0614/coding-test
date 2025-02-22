def solution(s):
    # 문자열을 리스트로 변환 -> sorted()로 내림차순 정렬 -> 문자열로 합침
    return ''.join(sorted(s, reverse=True))