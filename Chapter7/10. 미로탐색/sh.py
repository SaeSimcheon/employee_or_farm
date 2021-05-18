import sys
#sys.stdin=open('in1.txt','r')
base=[list(map(int,sys.stdin.readline().split())) for _ in range(7)]
base[0][0]=1
dx=[-1,0,1,0]
dy=[0,1,0,-1]

cnt=0
def DFS(x,y): ## 0,0에서 시작하면 될 듯?,for문써서 쭉쭉 나가면서 좌표를 바꿔주는 느낌으로 // DFS!
    global cnt 
    if x==y==6:
        cnt+=1
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<=6 and 0<=yy<=6 and base[xx][yy]==0: 
                base[xx][yy]=1
                DFS(xx,yy)
                base[xx][yy]=0

DFS(0,0)
print(cnt)

## 행,열 index에 따라 케이스 나누면서 if문 쓰고 있었는데 개트롤이었음
## 0<=xx<=6 and 0<=yy<=6 이런 식으로 index해결할수있다는게 제일 큰 소득이었음