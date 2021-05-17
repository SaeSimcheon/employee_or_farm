import sys
from collections import deque
#sys.stdin = open("input.txt", "rt")
n = int(input())
island = [list(map(int, input().split())) for i in range(n)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
cnt = 0
dQ = deque()
for i in range(n):
    for j in range(n):
        if island[i][j]==1:
            island[i][j]=0
            dQ.append((i,j))
            while dQ:
                now = dQ.popleft()
                for k in range(8):
                    x = now[0]+dx[k]
                    y = now[1]+dy[k]
                    if 0<=x<n and 0<=y<n and island[x][y]==1:
                        island[x][y]=0
                        dQ.append((x,y))
            cnt+=1 # 연결되어있는걸 모두 지나면 = while문 종료

print(cnt)

# 첫시도 100
# 이전 문제랑 비슷하게 이중 for문으로 하나하나 접근
# 섬이 있을때 그 주변 탐색 -> 주변에 1이 없으면 while 종료하고 cnt+=1


dx=[-1, -1, 0, 1, 1, 1, 0, -1]
dy=[0, 1, 1, 1, 0, -1, -1, -1]
n=int(input())
board=[list(map(int, input().split())) for _ in range(n)]
cnt=0
Q=deque()
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            board[i][j]=0
            Q.append((i, j))
            while Q:
                tmp=Q.popleft()
                for k in range(8):
                    x=tmp[0]+dx[k]
                    y=tmp[1]+dy[k]
                    if 0<=x<n and 0<=y<n and board[x][y]==1:
                        board[x][y]=0
                        Q.append((x, y))
            cnt+=1
print(cnt)
