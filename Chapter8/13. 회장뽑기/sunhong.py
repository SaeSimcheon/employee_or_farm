import sys
sys.stdin = open("input.txt", 'r')    
if __name__=="__main__":
    n=int(input())
    dis=[[100]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dis[i][i]=0
    while True:
        a, b=map(int, input().split())
        if a==-1 and b==-1:
            break
        dis[a][b]=1
        dis[b][a]=1

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dis[i][j]=min(dis[i][j], dis[i][k]+dis[k][j])

    res=[0]*(n+1)
    score=100
    for i in range(1, n+1):
        for j in range(1, n+1):
            res[i]=max(res[i], dis[i][j])
        score=min(score, res[i])
    out=[]
    for i in range(1, n+1):
        if res[i]==score:
            out.append(i)
    print("%d %d" %(score, len(out)))
    for x in out:
        print(x, end=' ')


#### 아 틀림
import sys
#sys.stdin=open('in1.txt')
n=int(sys.stdin.readline())
dy=[[9999]*n for _ in range(n)]
for i in range(n):
    dy[i][i]=0
base=[]
while True:
    a,b=map(int,sys.stdin.readline().split())
    if a==-1:
        break
    dy[a-1][b-1]=1

for k in range(n):
    for i in range(n):
        for j in range(n):
            dy[i][j]=min(dy[i][j],dy[i][k]+dy[k][j])

for i in range(n):
    for j in range(n):
        if dy[i][j]==9999:
            dy[i][j]=0

