import sys
#sys.stdin=open('in1.txt','r')
n=int(sys.stdin.readline())
base=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

d=[]
d.append(base[0][0])
for i in range(1,n):
    d.append(d[-1]+base[0][i])

f=list(map(list, zip(*base)))

dd=[]
dd.append(f[0][0])
for i in range(1,n):
    dd.append(dd[-1]+f[0][i])

dy=[d]+[[0]*n for _ in range(n-1)]

for i in range(1,n):
    dy[i][0]=dd[i]

for i in range(1,n):
    for j in range(1,n):
        if 0<=j-1<n or 0<=i-1<n:
            dy[i][j]=min(dy[i][j-1],dy[i-1][j])+base[i][j]

print(base[n-1][n-1])


## 틀림 어디가 틀렸는지 모르겠음