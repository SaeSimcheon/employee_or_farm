import sys
#sys.stdin=open('in1.txt','r')
n,m=map(int,sys.stdin.readline().split())

def DFS(L):
    global cnt
    if L==m:
        for i in range(m):
            print(res[i], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                DFS(L+1)
                ch[i]=0

cnt=0
ch=[0]*(n+1)
res=[0]*m
DFS(0)
print(cnt)
