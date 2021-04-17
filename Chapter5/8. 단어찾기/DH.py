'''
단어 찾기

차집합
'''
import sys

#sys.stdin = open("in1.txt","r")

k = int(input())

w = []
u = []
for i in range(k):
    w.append(input())
w = set(w)

for i in range(k-1):
    u.append(input())
u = set(u)
ans = w-u
print(ans.pop())

