import sys
#sys.stdin=open('in1.txt','r')
n=int(sys.stdin.readline())
base=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dx=[-1,0,1,0,1,-1,-1,1]
dy=[0,1,0,-1,1,-1,1,-1]

def DFS(x,y):
    global cnt
    base[x][y]=0
    cnt+=1 ## 
    for i in range(8):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<n and base[xx][yy]==1:
            DFS(xx,yy)

a=[]
for i in range(n):
    for j in range(n):
        if base[i][j]==1:
            cnt=0
            DFS(i,j)
            a.append(cnt)
            
print(len(a))
