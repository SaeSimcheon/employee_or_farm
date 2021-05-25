import sys
#sys.stdin=open('in1.txt','r')
n,m=map(int,sys.stdin.readline().split())
base=[[10000000]*n for _ in range(n)]
for i in range(n):
    base[i][i]=0
for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    base[a-1][b-1]=c

for k in range(n):
    for i in range(n):
        for j in range(n):
            base[i][j]=min(base[i][j],base[i][k]+base[k][j])

for i in range(n):
    for j in range(n):
        if base[i][j]==10000000:
            base[i][j]='M'

for x in base:
    for y in x:
        print(y,end=' ')
    print()
