import sys
#sys.stdin = open('input.txt','r')
n = int(input())
a = list(map(int, input().split()))
dy = [0]*n
dy[0]=1
for i in range(1,n):
    cnt = 0
    for j in range(i,0,-1):
        if a[j]<a[i] and dy[j]>cnt:
            cnt = dy[j]
    dy[i] = cnt+1
print(max(dy))

# 첫시도 100
# 오름차순 배열로 최대 몇개의 선을 연결하는지니까
# 이전 최대 증가수열이랑 똑같은 문제

import sys
sys.stdin = open("input.txt", 'r')
n=int(input())
arr=list(map(int, input().split()))
arr.insert(0,0)
dy=[0]*(n+1)
dy[1]=1
res=0
for i in range(2, n+1):
    max=0
    for j in range(i-1, 0, -1):
        if arr[j]<arr[i] and dy[j]>max:
            max=dy[j]
    dy[i]=max+1
    if dy[i]>res:
        res=dy[i]
print(res)