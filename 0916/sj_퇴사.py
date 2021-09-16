def DFS(L,p):
    global maximum
    if L>n:
        return
    if L==n:
        if maximum < p:
            maximum = p
    else:
        DFS(L+a[L][0],p+a[L][1])
        DFS(L+1,p)
if __name__=="__main__":
    n = int(input())
    a = [list(map(int,input().split())) for _ in range(n)]
    maximum = 0
    DFS(0,0)
    print(maximum)