import sys
# input.txt 파일은 현재 파이썬 파일과 같은 경로에 위치
sys.stdin = open("input.txt","r")
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# 문제
# : 10845 _ 큐
# https://www.acmicpc.net/problem/10845
# 등급
# : 실버 4
    
# 내가 파악한 요구사항
# : 자료구조 큐

# 실제 요구사항
# : 자료구조 큐
    
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <수도코드>
'''
n을 입력 받음
큐 리스트 생성
n개의 수만큼 명령어와 정수를 입력받으면서
큐 리스트에 대한 명령어 연산
'''

# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제풀이>
from collections import deque

n = int(input())
queue = deque()

for instruction in range(n):
    input_line = input().split()
    command = input_line[0]
    value = int(input_line[1]) if len(input_line) > 1 else None
    
    if command == "push":
        queue.append(value)
    elif command == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif command == "size":
        print(len(queue))
    elif command == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif command == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)

# -->> 시간초과 발생

# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <정답 및 다른풀이>

from collections import deque
import sys

input = sys.stdin.readline

n = int(input().strip())
queue = deque()
output = []

for _ in range(n):
    command = input().strip().split()

    if command[0] == "push":
        queue.append(int(command[1]))
    elif command[0] == "pop":
        output.append(queue.popleft() if queue else -1)
    elif command[0] == "size":
        output.append(len(queue))
    elif command[0] == "empty":
        output.append(0 if queue else 1)
    elif command[0] == "front":
        output.append(queue[0] if queue else -1)
    elif command[0] == "back":
        output.append(queue[-1] if queue else -1)

sys.stdout.write("\n".join(map(str, output)) + "\n")