import sys
# input.txt 파일은 현재 파이썬 파일과 같은 경로에 위치
sys.stdin = open("input.txt","r")
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제>
# : 2667 _ 단지 번호 붙이기

# <등급>
# : 실버 1
    
# <내가 파악한 요구사항>
# : 그래프 탐색

# <실제 요구사항>
# : 그래프 이론, 그래프 탐색
#   너비 우선 탐색, 깊이 우선 탐색
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <수도코드>
'''
<입력>
n = 지도의 칸
지도입력

<방향키> 상, 하, 좌, 우
dx = [1,-1,0,0]
dy = [0,0,-1,1]

<초기설정>


<출력>
단지수
각 단지내 집의 수
'''
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제풀이>
# 입력
n = int(input())
apt = [ list(map(int,input().split())) for _ in range(n) ]

# 방향키
dx = [1,-1,0,0]
dy = [0,0,-1,1]

# 초기 설정
count = 0

# 탐색


# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <정답 및 다른풀이>
# DFS
# 입력
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# DFS 함수
def dfs(x, y):
    global count  # 단지 내 집의 개수를 세기 위한 변수
    graph[x][y] = 0  # 방문 처리
    count += 1

    # 네 방향 탐색
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 지도 범위를 벗어나지 않고, 방문하지 않은 집일 경우
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
            dfs(nx, ny)

# 결과 저장
result = []

# 모든 위치 탐색
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:  # 집이 있는 곳이라면
            count = 0
            dfs(i, j)  # 단지 탐색 시작
            result.append(count)

# 결과 출력
result.sort()  # 단지 크기 오름차순 정렬
print(len(result))  # 단지 수 출력
for r in result:
    print(r)

#--------------------------------------#--------------------------------------#--------------------------------------

# BFS
from collections import deque

# 입력
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 함수
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0  # 방문 처리
    count = 1  # 단지 크기

    while queue:
        x, y = queue.popleft()

        # 네 방향 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 지도 범위를 벗어나지 않고, 방문하지 않은 집일 경우
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0  # 방문 처리
                queue.append((nx, ny))
                count += 1

    return count

# 결과 저장
result = []

# 모든 위치 탐색
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:  # 집이 있는 곳이라면
            result.append(bfs(i, j))  # BFS로 단지 탐색

# 결과 출력
result.sort()  # 단지 크기 오름차순 정렬
print(len(result))  # 단지 수 출력
for r in result:
    print(r)

# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제를 통한 학습 내용>