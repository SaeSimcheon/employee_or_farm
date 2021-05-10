import sys
#sys.stdin=open('in1.txt','r')
c,n=map(int,sys.stdin.readline().split())
base=[int(sys.stdin.readline()) for _ in range(n)]
base.sort(reverse=True)
w=0
def DFS(L,s,t):
    global w
    if s+total-t<w:
        return
    if s>c:
        return
    w=max(s,w)
    if L==n: 
        return
    DFS(L+1,s+base[L],t+base[L])
    DFS(L+1,s,t+base[L])
total=sum(base)
DFS(0,0,0)
print(w)


## cut off 의 중요성, 필요 없는 연산을 찾아내서 없애주는 게 중요
## L,s로만 함수 짰을 때는 80점밖에 안 나옴
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

