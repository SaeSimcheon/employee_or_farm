import sys
#sys.stdin = open("input.txt", "rt")
'''def DFS(x,y):
    global cnt
    M[x][y] = 0
    for i in range(4):
        Dx = x+dx[i]
        Dy = y+dy[i]
        if 0 <= Dx <= n-1 and 0 <= Dy <= n-1 and M[Dx][Dy] == 1:
            cnt+=1
            DFS(Dx,Dy)

if __name__ == "__main__":
    n = int(input())
    M = [list(map(int, input())) for i in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    res = []
    for a in range(n):
        for b in range(n):
            if M[a][b] == 1:
                cnt = 1
                DFS(a,b)
                res.append(cnt)
    print(len(res))
    for j in res:
        print(j)'''

# 첫시도 20점
# 뭔가 보완해야할게 있나봄

'''def DFS(x,y):
    global cnt
    M[x][y] = 0
    for i in range(4):
        Dx = x+dx[i]
        Dy = y+dy[i]
        if 0 <= Dx <= n-1 and 0 <= Dy <= n-1 and M[Dx][Dy] == 1:
            cnt+=1
            DFS(Dx,Dy)

if __name__ == "__main__":
    n = int(input())
    M = [list(map(int, input())) for i in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    res = []
    for a in range(n):
        for b in range(n):
            if M[a][b] == 1:
                cnt = 1
                DFS(a,b)
                res.append(cnt)
    print(len(res))
    res.sort()
    for j in res:
        print(j)'''

# 두번째 100
# 오름차순 조건을 못봤음
# 문제를 잘 읽자...


# 이 문제는 DFS, BFS 둘다 해결 가능
# DFS version
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
def DFS(x, y):
    global cnt
    cnt+=1
    board[x][y]=0
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<n and board[xx][yy]==1:
            DFS(xx, yy)

if __name__=="__main__":
    n=int(input())
    board=[list(map(int, input())) for _ in range(n)]
    res=[]
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                cnt=0
                DFS(i, j)
                res.append(cnt)
    print(len(res))
    res.sort()
    for x in res:
        print(x)

# BFS version
from collections import deque
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
n=int(input())
board=[list(map(int, input())) for _ in range(n)]
cnt=0
res=[]
Q=deque()
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            board[i][j]=0
            Q.append((i, j))
            cnt=1
            while Q:
                tmp=Q.popleft()
                for k in range(4):
                    x=tmp[0]+dx[k]
                    y=tmp[1]+dy[k]
                    if x<0 or x>=n or y<0 or y>=n or board[x][y]==0:
                        continue
                    board[x][y]=0
                    Q.append((x, y))
                    cnt+=1
            res.append(cnt)

print(len(res))
res.sort()
for x in res:
    print(x)

# 반성점
# 1. 오름차순 조건을 생각을 못함, 문제를 꼼꼼히 읽고 풀자

# 배운점
# 1. input에서 int자료가 띄어쓰기가 안되어있으면 input().split()으로 불러오지 않고, input()으로만 불러온다