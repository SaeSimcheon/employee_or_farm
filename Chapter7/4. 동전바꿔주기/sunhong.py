import sys
#sys.stdin=open('in1.txt','r')
t=int(sys.stdin.readline())
k=int(sys.stdin.readline())
price=[]
n=[]
for _ in range(k):
    p,ni=map(int,sys.stdin.readline().split())
    price.append(p)
    n.append(ni)

def DFS(L,sum):
    global cnt
    if L==k:
        if sum==t:
            cnt+=1
    if sum>t:
        return
    else:
        for i in range(n[L]+1):
            DFS(L+1,sum+(price[L]*i))

cnt=0
DFS(0,0)
print(cnt)

### 동전 갯수 세가면서 DFS로 푸려고 하다가 삽질 겁나 했음. Level 단위로 유연하게 생각하는 게 중요한 듯

cnt=0
cc=[]
## check=[0]*k ni를 체크하기 위한 list
def DFS(sum,check):
    global cnt
    global cc
    if sum==t and check not in cc:
        cnt+=1
        cc.append(check)
    print(check,sum,cnt)
    if sum>t:
        return
    else:
        for i in range(k):
            if check[i]<n[i]:
                check[i]+=1
                DFS(sum+price[i],check)
                check[i]-=1


