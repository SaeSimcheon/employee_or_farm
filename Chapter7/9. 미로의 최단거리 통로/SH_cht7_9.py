import sys
sys.stdin=open("input.txt", "r")
from collections import deque
seq = [[1,*list(map(int,input().split())),1] for _ in range(7)]


add=[1]*9

seq.insert(0,add)
seq.append(add)


start = [1,1,0]


que=deque(list())
que.append(start)

out = list()
i=0
while True:
    if len(que) ==0:
        print(-1)
        break
    a = que.popleft()
    
    if a[0:2] == [1,1]:
        seq[1][1] =1
    
    if a[0:2] == [7,7]:
        print(a[2])
        break
    else:
        if seq[a[0]+1][a[1]] ==1 :
            pass
        else :
            
            seq[a[0]+1][a[1]] =1
            candidate = [a[0] + 1,a[1],a[2]+1]
   
            que.append(candidate)
            
        if seq[a[0]][a[1]+1] ==1 :
            pass
        else:
            
            seq[a[0]][a[1]+1] =1
            candidate = [a[0],a[1]+1,a[2]+1]
            que.append(candidate)
            
            
        if seq[a[0]-1][a[1]] ==1 :
            pass
        else:
            seq[a[0]-1][a[1]] =1
            candidate = [a[0] - 1,a[1],a[2]+1]
            que.append(candidate)
            
            
            
        if seq[a[0]][a[1]-1] ==1 :
            pass
        else:
            
            seq[a[0]][a[1]-1] =1
            candidate = [a[0],a[1]-1,a[2]+1]

            que.append(candidate)
      




