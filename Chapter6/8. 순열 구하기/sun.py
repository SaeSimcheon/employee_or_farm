import sys
#sys.stdin=open('in1.txt','r')
n,m=map(int,sys.stdin.readline().split())
def DFS(L):
    global cnt
    if L==m:
        cnt+=1
        for x in a:
            print(x,end=' ')
        print()
    else:
        for i in range(1,n+1):
            a[L]=i
            DFS(L+1)
a=[0]*m
cnt=0
DFS(0)
print(cnt)


## 처음에 check list만들생각부터했음, 너무 복잡한쪽으로생각하려는 경향이 큼