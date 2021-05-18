import sys
from collections import deque
sys.stdin = open("input.txt","rt")

N= int(input())



seq=[list(map(int,input().split())) for _ in range(N)]



cnt = 0
dx=[-1,0,1,0,-1,-1,1,1]
dy=[0,-1,0,1,-1,1,-1,1]

que = deque(list())

res = list()
for i in range(N):
    for j in range(N):
        if seq[i][j] ==1 :
            seq[i][j] =0
            que.append((i,j))
            cnt=1
            while que :
                element=que.popleft()
                for ii in range(8):
                    xx = element[0] + dx[ii]
                    yy = element[1] + dy[ii]

                    if not (0<= xx < N and 0 <= yy < N and seq[xx][yy] == 1):
                        continue
                    seq[xx][yy] = 0
                    
                    que.append((xx,yy))
                    cnt +=1
            res.append(cnt)
                    

        
                

print(len(res))


