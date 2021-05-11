import sys
from collections import deque
sys.setrecursionlimit(10**6)

#sys.stdin = open("in5.txt")

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

cnt = 0
res = 0

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def DFS(x,y,h):
    ch[x][y] = 1

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and arr[xx][yy] > h:
            DFS(xx,yy,h)
            
for h in range(100):
    ch = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if ch[i][j] == 0 and arr[i][j] > h:
                cnt += 1
                DFS(i,j,h)
    res = max(res,cnt)
    if cnt == 0 :
        break
print(res)
