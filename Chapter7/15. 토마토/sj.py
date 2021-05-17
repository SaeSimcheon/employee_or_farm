import sys
from collections import deque
#sys.stdin = open("input.txt", "rt")
m, n = map(int,input().split())
storage = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
dQ = deque()
if len(set(sum(storage,[]))) != 3 and sum(set(sum(storage,[]))) == 0: # 조건에 맞게 처음에 0,1,-1이 아니면 0 출력
    print(0)
else: # 아니면 BFS써서 다 돌때까지의 날짜를 세기
    for i in range(n):
        for j in range(m):
            if storage[i][j]==1:
                dQ.append((i,j))
    while dQ:
        for _ in range(len(dQ)):
            now = dQ.popleft()
            for k in range(4):
                x = now[0]+dx[k]
                y = now[1]+dy[k]
                if 0<=x<n and 0<=y<m and storage[x][y]==0:
                    storage[x][y]=1
                    dQ.append((x,y))
        if dQ:
            cnt+=1
    if len(set(sum(storage,[]))) == 2: # 다 돌고 나서 1,-1만 있으면 답 출력
        print(cnt)
    else: # 0도 존재한다면 -1 출력
        print(-1)

# 첫시도 80 (5번 time limit)

# while문이 끝나고 나면 다시 1,-1만 있는지 확인 후 답 출력
# 처음에는 이중 for문안에 while을 넣었는데 그러면 날짜를 셀수가 없어서 밖으로 뺐음
# while 안에서 dQ가 len>1일때 날짜 세는걸로

# 근데 아무리 생각해도 중간에 끊어줄게 생각이 안남 ㅅㅂ

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
n, m=map(int, input().split())
board=[list(map(int, input().split())) for _ in range(m)]
Q=deque()
dis=[[0]*n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if board[i][j]==1:
            Q.append((i, j))
while Q:
    x, y=Q.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<m and 0<=ny<n and board[nx][ny]==0:
            board[nx][ny]=1
            dis[nx][ny]=dis[x][y]+1
            Q.append((nx, ny))
flag=1
for i in range(m):
    for j in range(n):
        if board[i][j]==0:
            flag=0
result=0
if flag==1:
    for i in range(m):
        for j in range(n):
            if dis[i][j]>result:
                result=dis[i][j]
    print(result)
else:
    print(-1)

# 5번은 limit 날수도 있다고 함
# distance 로 matrix를 만드는거나 나처럼 cnt를 세는거나 다를건 없을듯

# 배운점
# 1. 날짜를 체크하는 matrix를 새롭게 만드는 것도 답이 될수 있겠다