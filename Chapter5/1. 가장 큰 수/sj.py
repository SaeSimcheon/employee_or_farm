import sys
#sys.stdin=open("input.txt", "rt")
'''a, m = input().split()
n = len(a)
m = int(m)
length = n-m
a = [int(i) for i in a]
largest = []
for i in a:
    while m>0 and largest and largest[-1]<i:
        largest.pop()
        #print(largest)
        m-=1
        #print(m)
    largest.append(i)
    #print(largest)
if m>0:
    largest = largest[:length]
for i in largest:
    print(i,end='')'''

# 첫시도 100
# stack 이라니까,,, 뭔가 쌓아간다는 느낌으로
# 마지막 원소를 다음꺼랑 비교하면서 크면 빼고 아니면 넣고
# if 안에 while을 넣었는데 안되서 그냥 while로만 짬
# 근데 마지막이 다 작으면 길이가 안되서 마지막 if문 추가

# stack 자료 구조형
# Last in / First out
# 출구와 입구가 한곳 / 제일 나중에 들어간게 먼저 나온다
# list.pop을 이용 / stack에 넣고 조건에 따라 빼고 반복


# list slice에서 [0:-2]는 뒤에 두개

num, m = map(int, input().split())
num = list(map(int, str(num))) # 한개씩 접근해서 int
stack = []
for x in num:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1 # 지우고나서 지울수있는 수 m을 하나씩 줄이기
    stack.append(x)
if m!=0:
    stack = stack[:-m] # 뒤쪽의 m개의 자료 제거
res = ''.join(map(str,stack))
print(res)

# 느낀점
# 1. 접근은 비슷하게 했음

# 배운점
# 1. stack 자료 구조형 -> last in first out
# 2. stack 조건이면 비어있으면 False
# 3. list slice에서 [:-m]는 뒤에서 m개 제거
# 4. ''.join(map(str,stack)) 이면 stack을 str로 바꾸고 합치기
