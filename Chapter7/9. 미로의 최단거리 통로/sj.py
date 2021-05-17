import sys
from collections import deque
#sys.stdin = open("input.txt", "rt")
'''a = [list(map(int, input().split())) for i in range(7)]
b = [[0]*7 for _ in range(7)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dQ = deque()
dQ.append((0,0))
a[0][0]=1  #첫 출발에 표시
while dQ:
    now = dQ.popleft()
    for i in range(4):
        x = now[0]+dx[i]
        y = now[1]+dy[i]
        if (0<=x and x<=6) and (0<=y and y<=6) and a[x][y]==0:
            a[x][y] = 1
            b[x][y] = b[now[0]][now[1]]+1
            dQ.append((x,y))
if b[6][6] == 0:
    print(-1)
else:
    print(b[6][6])
'''
# 강의 첫부분 보고 해결
# 0으로 초기화된 board를 바탕으로 이동하면서 이동수를 표시

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
board=[list(map(int, input().split())) for _ in range(7)]
dis=[[0]*7 for _ in range(7)]
Q=deque()
Q.append((0, 0))
board[0][0]=1
while Q:
    tmp=Q.popleft()
    for i in range(4):
        x=tmp[0]+dx[i]
        y=tmp[1]+dy[i]
        if 0<=x<=6 and 0<=y<=6 and board[x][y]==0:
            board[x][y]=1
            dis[x][y]=dis[tmp[0]][tmp[1]]+1
            Q.append((x, y))
if dis[6][6]==0:
    print(-1)
else:
    print(dis[6][6])

# 반성점
# 1. 쉬운 문제였지만 거리를 어떻게 표시하는데 어려움이 있었음, 좀더 고민해봤어야 했다

