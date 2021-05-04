import sys
#sys.stdin=open('in1.txt','r')
c,n=map(int,sys.stdin.readline().split())
base=[int(sys.stdin.readline()) for _ in range(n)]
total=sum(base)
weight=0
def DFS(L,summ):
    global weight
    if L==n:
        return
    if summ>=total-c:
        a=total-summ
        weight=max(a,weight)
    else: ## c 넘어가는 상황
        pass

    DFS(L+1,summ+base[L])
    DFS(L+1,summ)
    
DFS(0,0)
print(weight) 

### 5번 input time limit exceeded, 80점

