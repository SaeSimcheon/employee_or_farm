import sys
sys.stdin=open("input.txt", "r")
from collections import deque
seq = [[1,*list(map(int,input().split())),1] for _ in range(7)]


add=[1]*9

seq.insert(0,add)
seq.append(add)

#print(seq)

cnt=0
def DFS(i,j,data):
    global cnt
#    print(i,j,cnt)
    if (i == 1) & (j == 1) : 
        seq[1][1] =1
    if (i == 7) & (j == 7) : 
        cnt+=1
        return
    
    else :
        if data[i+1][j] ==0 :
            data[i+1][j] =1
            DFS(i+1,j,data)
            data[i+1][j] =0

        if data[i][j+1] ==0 :
            data[i][j+1] =1
            DFS(i,j+1,data)
            data[i][j+1] =0

        
            
        if data[i-1][j] ==0 :
            data[i-1][j] =1
            DFS(i-1,j,data)
            data[i-1][j] =0
        
        if data[i][j-1] ==0 :
            data[i][j-1] =1
            DFS(i,j-1,data)
            data[i][j-1] =0
DFS(1,1,seq)
print(cnt)