def solution(triangle):
    n = len(triangle)
    
    # DP 테이블 업데이트 (아래에서 위로)
    for i in range(n - 2, -1, -1):  # 끝에서 두 번째 줄부터 시작
        for j in range(len(triangle[i])):  # 현재 행의 원소 개수만큼 반복
            # 아래쪽 두 개의 값 중 더 큰 값을 현재 위치에 더함
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

    # 최종적으로 꼭대기의 값이 최대 경로 합
    return triangle[0][0]