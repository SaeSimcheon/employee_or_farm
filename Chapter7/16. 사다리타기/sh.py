##이건 밑에서 올라가야  
import sys
#sys.stdin=open('in1.txt','r')
n=10
base=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
ch=[[0]*n for _ in range(n)]

idx=base[9].index(2)# 9,5에서 시작해서 쭉쭉올라가면됨

def DFS(x, y):
    ch[x][y]=1
    if x==0:
        print(y)
    else:
        if y-1>=0 and base[x][y-1]==1 and ch[x][y-1]==0:
            DFS(x, y-1)
        elif y+1<10 and base[x][y+1]==1 and ch[x][y+1]==0:
            DFS(x, y+1)
        else:
            DFS(x-1, y)

DFS(9,idx)
