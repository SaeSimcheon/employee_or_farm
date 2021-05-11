import sys
#sys.stdin=open('in1.txt','r')
n=int(sys.stdin.readline())
base=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

h=0
def DFS(L,price): ## L: day, price: 휴가비
    global h    
    if L==n :
        h=max(h,price)
    else:
        if L+base[L][0]<=n:
            DFS(L+base[L][0],price+base[L][1])
        DFS(L+1,price)
DFS(0,0)
print(h)

## 이거 6장 10번 조합구하는거처럼 풀어볼랬는데 실패함
h=0
def DFS(L,price): 
    global h    
    if L>n :
        h=max(h,price)
    else:
        for i in range(L,n):
#            print(L,price)
            DFS(L+base[i][0],price+base[i][1]) 
DFS(0,0)
print(h)
