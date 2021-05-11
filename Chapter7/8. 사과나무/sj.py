import sys
from collections import deque
#sys.stdin = open("input.txt", "rt")
n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
ch = [[0]*n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
L = 0
sum = 0
dQ = deque()
sum += a[n//2][n//2]
dQ.append((n//2,n//2))
ch[n//2][n//2]=1  #첫 출발에 표시
while True:
    if L==n//2:
        break
    for i in range(len(dQ)): # next가 tuple 값을 하나씩 돈다
        now = dQ.popleft()
        for j in range(4):
            x = now[0]+dx[j]
            y = now[1]+dy[j]
            if ch[x][y]==0:
                sum+=a[x][y]
                ch[x][y]=1
                dQ.append((x,y))
    L+=1
print(sum)
