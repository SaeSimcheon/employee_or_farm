import sys
#sys.stdin=open('in1.txt','r')
n,k=map(int,sys.stdin.readline().split())
b=[0]+list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())

##조합구하기
def DFS(L,d):
    global cnt
    if L==k :
        if sum(a)%m==0:
            cnt+=1
    else:
        for i in range(d,n+1):
            a[L]=b[i]
            DFS(L+1,i+1) 

a=[0]*k
cnt=0
DFS(0,1)
print(cnt)
