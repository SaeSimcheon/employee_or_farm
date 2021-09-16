n=int(input())
base=[list(map(int,input().split())) for _ in range(n)]
h=0
def DFS(L,price): 
    global h    
    if L==n :
        h=max(h,price)
    else:
        if L+base[L][0]<=n:
            DFS(L+base[L][0],price+base[L][1])
        DFS(L+1,price)
DFS(0,0)
print(h)
