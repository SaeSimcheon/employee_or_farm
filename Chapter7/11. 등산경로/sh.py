import sys
#sys.stdin=open('in1.txt','r')
n=int(sys.stdin.readline())
base=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
ch=[[0]*n for _ in range(n)]
start=2470000000000000
for i in range(n):
    for j in range(n):
        if base[i][j]<start:
            start=base[i][j]
            start_x=i
            start_y=j
            
mok=0
for i in range(n):
    for j in range(n):
        if base[i][j]>mok:
            mok=base[i][j]
            mok_x=i
            mok_y=j
            
ch[start_x][start_y]=1

## DFS
cnt=0
def DFS(x,y): 
    global cnt 
    if x==mok_x and y==mok_y:
        cnt+=1
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<n and 0<=yy<n and base[xx][yy]>base[x][y]: ## 여기 조건에 ch[xx][yy] ==0 넣어줬어야 함. 근데 빼도 100점나옴. 데이터 덕분인듯
                ch[xx][yy]=1
                DFS(xx,yy)
                ch[xx][yy]=0


DFS(start_x,start_y)
print(cnt)
