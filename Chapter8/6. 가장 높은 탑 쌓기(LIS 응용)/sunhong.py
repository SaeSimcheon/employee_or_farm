import sys
#sys.stdin=open('in2.txt','r')
n=int(sys.stdin.readline())
base=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
base.sort(reverse=True)

dy=[0]*n
dy[0]=base[0][1]

### 아 이건 순서 바꿔도 되는구나
for i in range(1,n):
    height=0
    for j in range(0,i):
        if base[i][2]<base[j][2]:
            height=max(height,dy[j]+base[i][1])
#            print(i,j,height)
    dy[i]=max(base[i][1],height)
#    print(i,dy)

print(max(dy))


## 수열처럼 순서 안바뀌게 풀어서 틀린 40점짜리

import sys
#sys.stdin=open('in1.txt','r')
n=int(sys.stdin.readline())
base=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dy=[0]*n
dy[0]=base[0][1]

for i in range(1,n):
    height=0
    for j in range(0,i):
        if base[i][0]<base[j][0] and base[i][2]<base[j][2]:
            height=max(height,dy[j]+base[i][1])
    dy[i]=max(base[i][1],height)

print(max(dy))
