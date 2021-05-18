import sys
from collections import deque
#sys.stdin=open('in1.txt','r')
base=[list(map(int,sys.stdin.readline().split())) for _ in range(7)]
base[0][0]=1
ch=[[0]*7 for _ in range(7)]
d=deque()
d.append((0,0))
dx=[-1,0,1,0]
dy=[0,1,0,-1]

#L=1
while d:
    #print('{}th loop'.format(L))
    coordi=d.popleft()
    if coordi==(6,6):
        break
    x=coordi[0]
    y=coordi[1]
    for j in range(4):
        xx=x+dx[j]
        yy=y+dy[j]
        if 0<=xx<=6 and 0<=yy<=6 and base[xx][yy]==0:
            ch[xx][yy]=ch[x][y]+1
            base[xx][yy]=2
            d.append((xx,yy))
#    L+=1


if ch[6][6]!=0:
    print(ch[6][6])
else:
    print(-1)

## 억지로 짜긴 했는데 이게 모든 케이스를 포괄하는 예외없는 코드가 맞나..? 잘 이해가 안됨 막 경로수 덮어쓰고 그런 경우 안 일어나나?