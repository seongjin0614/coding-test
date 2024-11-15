import sys
# input.txt 파일은 현재 파이썬 파일과 같은 경로에 위치
sys.stdin = open("input.txt","r")
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제>
# : 1874 _ 스택 수열
# https://www.acmicpc.net/problem/1874
# <등급>
# : 실버 2
# <내가 파악한 요구사항>
# : 자료구조 - 스택
# <실제 요구사항>
# : 자료구조 - 스택
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <수도코드>
'''
n 의 개수를 입력 받음.
수열의 결과?를 입력 받음.

1 부터 스택에 순차적으로 push 하다가
수열의 첫번째와 일치한다면 pop 그리고
수열의 다음을 비교(인덱스?)

push 할때마다 + 출력
pop 할때마다 - 출력
예외처리 'no' 반환

결과 리스트에 +, - 를 추가해 리스트를 출력하는 방법?
'''
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제풀이>
n = int(input())
progression = [int(input()) for _ in range(n)]

stack_list = []
result = []
current = 1
possible = True

for number in progression:
    while current <= number:
        stack_list.append(current)
        result.append("+")
        current += 1
        
    if stack_list[-1] == number:
        stack_list.pop()
        result.append("-")
    else:
        possible = False
        break
        
if possible:
    print("\n".join(result))
else:
    print("NO")



# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <정답 및 다른풀이>



# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제를 통한 학습 내용>
'''
join()
함수는 문자열들을 특정 구분자로 연결하여 하나의 문자열로 만드는 함수입니다. 주로 리스트나 튜플에 있는 문자열들을 결합할 때 사용됩니다.

- 기본 문법 -
'구분자'.join(문자열_리스트)

- 기본 예제: 공백을 구분자로 사용하여 문자열들을 연결 -
words = ["Hello", "world", "Python"]
sentence = " ".join(words)
print(sentence)  # 출력: "Hello world Python"

- 줄바꿈(\n)을 사용하여 연결: 각 문자열을 줄바꿈으로 연결하여 여러 줄로 출력 -
lines = ["First line", "Second line", "Third line"]
paragraph = "\n".join(lines)
print(paragraph)
# 출력:
# First line
# Second line
# Third line

- 콤마로 구분하여 연결: 리스트의 각 요소를 쉼표로 구분하여 연결 -
items = ["apple", "banana", "cherry"]
fruits = ", ".join(items)
print(fruits)  # 출력: "apple, banana, cherry"
'''