'''
토마토(BFS 활용)
1 : 익은 토마토
0 : 익지 않은 토마토
-1 : 토마토 x 
'''

import sys
from collections import deque

#sys.stdin = open("in1.txt")

m,n = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(n)]

Q = deque()
C_0 = 0
day = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            Q.append((i,j))
        if arr[i][j] == 0:
            C_0 += 1

dx = [0,1,0,-1]
dy = [1,0,-1,0]

while Q:
    tmp = Q.popleft()

    for _x,_y in zip(dx,dy):
        x = tmp[0] + _x
        y = tmp[1] + _y

        if 0 <= x < n and 0 <= y < m and arr[x][y] == 0:
            arr[x][y] = arr[tmp[0]][tmp[1]] + 1
            Q.append((x,y))
            C_0 -=1

            if day < arr[x][y]:
                day = arr[x][y]

if C_0 == 0:
    print(day - 1)
else :
    print(-1)
