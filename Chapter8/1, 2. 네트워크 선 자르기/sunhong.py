import sys
#sys.stdin=open('in1.txt','r')
n=int(sys.stdin.readline())

dy=[0]*n
dy[0]=1
dy[1]=2

for i in range(2,n):
    dy[i]=dy[i-1]+dy[i-2]

print(dy[-1])

## DFS로 해봣는데/maximum recursion depth exceeded in comparison

import sys
#sys.stdin=open('in1.txt','r')
n=int(sys.stdin.readline())

def DFS(x):
    global cnt
    if x==n:
        cnt+=1
    else:
        DFS(x+1)
        DFS(x+2)

cnt=0
DFS(0)
print(cnt)

