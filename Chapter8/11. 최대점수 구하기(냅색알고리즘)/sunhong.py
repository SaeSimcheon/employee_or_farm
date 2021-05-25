import sys
#sys.stdin=open('in1.txt','r')
n,m=map(int,sys.stdin.readline().split())
base=[list(map(int,sys.stdin.readline().split())) for _ in range(n)] # 점수, 시간

dy=[0]*(m+1)

for i in range(n):
    time=base[i][1]
    score=base[i][0]
    for j in range(m,time-1,-1):
        dy[j]=max(dy[j],dy[j-time]+score)

print(dy[-1])
