import sys
# input.txt 파일은 현재 파이썬 파일과 같은 경로에 위치
sys.stdin = open("input.txt","r")
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제>
# : 1018 _ 체스판 다시 칠하기
# https://www.acmicpc.net/problem/1018
# <등급>
# : 실버 4
    
# <내가 파악한 요구사항>
# : 이차원 행렬, dp

# <실제 요구사항>
# : 브루트포스 알고리즘
    
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <수도코드>
'''
입력값을 이차원배열로 받음.
visited list를 이차원배열 크기로 0으로 초기화
이차원 배열 인덱스를 이용해서 상하좌우가 본인가 같다면
0을 1로 설정?

조건 1. 최솟값을 구하는 문제
'''
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제풀이>

n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

def count_changes(board, start_row, start_col, start_color):
    changes = 0
    for i in range(8):
        for j in range(8):
            expected_color = start_color if (i+j)%2 == 0 else('B' if start_color == 'W' else 'W')
            if board[start_row+i][start_col+i] != expected_color:
                changes +=1
    return changes


# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <정답 및 다른풀이>
'''
start_row, start_col: 8×8 체스판의 시작 위치.
• start_color: 시작 색상(B 또는 W).
• 동작:
• 예상 색상과 실제 색상이 다르면 changes를 증가.
'''
def count_changes(board, start_row, start_col, start_color):
    changes = 0
    for i in range(8):
        for j in range(8):
            # 현재 칸의 예상 색상
            expected_color = start_color if (i + j) % 2 == 0 else ('B' if start_color == 'W' else 'W')
            # 체스판이 예상 색상과 다르면 수정 필요
            if board[start_row + i][start_col + j] != expected_color:
                changes += 1
    return changes

# 입력
n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

min_changes = float('inf')  # 무한대

# 모든 8x8 체스판에 대해 검사
for i in range(n - 7):      # 가능한 시작 행
    for j in range(m - 7):  # 가능한 시작 열
        # 두 가지 색상 기준으로 수정 횟수 계산
        changes_with_black_start = count_changes(board, i, j, 'B')
        changes_with_white_start = count_changes(board, i, j, 'W')
        
        # 최소 변경 횟수 갱신
        min_changes = min(min_changes, changes_with_black_start, changes_with_white_start)

print(min_changes)
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제를 통한 학습 내용>
'''
strip() 메서드

• strip()은 문자열의 양쪽 끝에서 특정 문자(기본적으로 공백 문자)를 제거하는 메서드입니다.
• 기본적으로 문자열 앞뒤의 공백, 탭 문자(\t), 줄바꿈 문자(\n)를 제거합니다.

사용법
string.strip([chars])

매개변수:
• chars: 제거할 문자들을 지정합니다.
• 생략하면 공백 문자(스페이스, 탭, 줄바꿈 등)를 제거합니다.

반환값:
• 문자열의 양쪽 끝에서 지정된 문자를 제거한 새로운 문자열을 반환합니다.


예제
1. 공백 문자 제거
s = "   Hello, World!   "
print(s.strip())  # 출력: "Hello, World!"

2. 특정 문자 제거
s = "---Hello, World!---"
print(s.strip("-"))  # 출력: "Hello, World!"

3. 문자열 내부의 공백은 제거되지 않음
s = "   Hello,    World!   "
print(s.strip())  # 출력: "Hello,    World!"
'''