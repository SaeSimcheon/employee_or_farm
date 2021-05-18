import sys
#sys.stdin=open('in1.txt','r')
n=int(sys.stdin.readline())
b=[]
for _ in range(n):
    b.append(str(sys.stdin.readline().strip()))

base=[]
for i in b:
    x=[]
    for j in range(n):
        x.append(int(i[j]))
    base.append(x)
    
    
#ch=[[0]*n for _ in range(n)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def DFS(x,y):
    global cnt
    base[x][y]=0
    cnt+=1 ## 
    for i in range(4):
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
a.sort()
for x in a:
    print(x,end='')
