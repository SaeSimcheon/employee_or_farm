'''
안전영역(BFS)
'''

import sys
from collections import deque


#sys.stdin = open("in5.txt")
sys.setrecursionlimit(10**6)
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
'''
n = 5
arr = [[6,8,2,6,2],
       [3,2,3,4,6],
       [6,7,3,3,2],
       [7,2,5,3,6],
       [8,9,5,2,7]]
'''
ans = -121
for std in range(0,100):
    pos = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] > std:
                pos.append((i,j))

    if len(pos) == 0:
        break
    
    cnt = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    while pos:
        Q = deque()
        Q.append(pos.pop(0))
        while Q:
            tmp = Q.pop()
            for x_,y_ in zip(dx,dy):
                x = tmp[0] + x_
                y = tmp[1] + y_
                if 0 <= x < n and 0 <= y < n and (x,y) in pos:
                    Q.append((x,y))
                    pos.pop(pos.index((x,y)))

        cnt += 1

    if cnt > ans:
        ans = cnt
print(ans)

