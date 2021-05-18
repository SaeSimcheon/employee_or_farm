import sys
from collections import deque
import copy
sys.stdin = open("input.txt","rt")

M,N= map(int,input().split())

seq_=[list(map(int,input().split())) for _ in range(N)]

sol = [[ 1 if element >-1  else -1 for element in row] for row in seq_  ]

#print(sol == sol)



dx = [-1,0,1,0]
dy = [0,-1,0,1]

que = deque()
new = list()
cnt = 0






while sol != seq_ :
    
    for i in range(N):
        for j in range(M):
            if seq_[i][j] == 1 :
                #print("here")
                que.append((i,j))
    #print(cnt)
#    print(new)
#    print(que)
    new = list()
    
    container= copy.deepcopy(seq_)
    #print(container == seq_)
    while que:
        element=que.popleft()
     #   print(seq_)
        for ii in range(4):
            xx = element[0] + dx[ii]
            yy = element[1] + dy[ii]
            if not (0<= xx < N and 0 <= yy < M and seq_[xx][yy] ==0):
                continue
            seq_[xx][yy] = 1
            new.append((xx,yy))
    #print(container == seq_,cnt)
    if container == seq_ :
        cnt= -1
        break
    cnt +=1
    #print(cnt)

print(cnt)