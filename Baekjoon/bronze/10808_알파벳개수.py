import sys
# input.txt 파일은 현재 파이썬 파일과 같은 경로에 위치
sys.stdin = open("input.txt","r")
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제>
# : 10808_알파벳개수

# <등급>
# : 브론즈 4
    
# <내가 파악한 요구사항>
# : 배열탐색

# <실제 요구사항>
# : 베열, 문자열
    
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <수도코드>
# 알파벳 수만큼의 원소를 가진 배열 생성
# 입력값을 순회하면서 같은 알파벳이 있으면 카운터 증가
# 최종적으로 알파벳의 인덱스순서에 생성된 배열에 카운터 값 입력
# 생성 배열 출력
# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제풀이>
word = input()

alphabet = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
count = [0] * 26

for i in range(len(word)):
  for j in range(len(alphabet)):
    if word[i] == alphabet[j]:
      count[j] += 1

print(count)

# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <정답 및 다른풀이>

# ------------------------------------------------------------------------------------------------------------------------------------------------   
# <문제를 통한 학습 내용>