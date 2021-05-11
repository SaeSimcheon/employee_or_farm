import sys
sys.stdin=open("input.txt", "r")
def DFS(L, sum):
    global res
    if L==n:
        if 0<sum<=s:
            res.add(sum)
    else:
        DFS(L+1, sum+base[L])
        DFS(L+1, sum-base[L])
        DFS(L+1, sum)

s=sum(base)    
res=set()
DFS(0, 0)
print(s-len(res))




import sys
#sys.stdin=open('in1.txt','r')
k=int(sys.stdin.readline())
base=list(map(int,sys.stdin.readline().split()))
base.sort()
s=sum(base)
a=list(range(2,s))

cnt=0
def DFS(L,sum,x):
    global cnt
    if L==k:
        return
    if sum==x:
        cnt+=1 ## 무게추로 x무게를 구현할 수 있으면 1 아니면 0
        return
    if sum<0:
        return
    else:
        DFS(L+1,sum+base[L],x)
        DFS(L+1,sum-base[L],x)
        DFS(L+1,sum,x)
        

ans=0
for x in a:
    cnt=0
    DFS(0,0,x)
    ans+=cnt
print(len(a)-ans)

### 실패함..set 활용할것
