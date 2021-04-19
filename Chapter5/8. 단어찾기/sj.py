import sys
#sys.stdin = open("input.txt", "rt")
'''n = int(input())
note = []
for i in range(n):
    note.append(input())
while len(note)>1:
    for j in range(n-1):
        poem = input()
        if poem in note:
            note.remove(poem)
print(note[0])'''

# 첫시도 100
# 이렇게 푸는게 맞는건지 모르겠따
# 강의 보고 판단하기

# dictionary 구조를 사용하면 아주 편리 / key : value 형태
n = int(input())
p = dict()
for i in range(n):
    word = input()
    p[word]=1
for i in range(n-1):
    word = input()
    p[word]=0 # key 값에 맞는거를 0으로 변경
for key, val in p.items():
    if val == 1:
        print(key)

# 배운점
# 1. dictionary 자료 구조 : key / value를 동시에 쓸때 아주 편리
# key를 비교해서 해당 key의 value를 변경하는게 가능