import sys
from collections import deque
import copy
sys.stdin = open("input.txt","rt")

N= int(input())

seq_=[list(map(int,input().split())) for _ in range(N)]



#print(seq)



dx = [-1,0,1,0]
dy = [0,-1,0,1]

que = deque()
cnt = 0



maximum=max([jj for ij in seq_ for jj in ij])
#print(maximum)
out = list()



for jj in range(1,maximum):
    res = list()
    
    seq = copy.deepcopy(seq_)
    
    for i in range(N):
        for j in range(N):
            if seq[i][j] > jj:
                #print(i,j)
                #print(seq[i][j])
                seq[i][j] =0
                cnt =1
                que.append((i,j))
                #print(i,j)
                while que:
                    element = que.popleft()
                    for ii in range(4):
                        xx = element[0] + dx[ii]
                        yy = element[1] + dy[ii]

                        if not (0 <= xx < N and 0 <= yy < N and seq[xx][yy] >jj) :
                            continue
                        seq[xx][yy]=0
                        que.append((xx,yy))
                        cnt+=1
                        #print(cnt)
                res.append(cnt)
                #print(res)
    out.append(len(res))

print(max(out))