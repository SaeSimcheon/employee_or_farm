import sys
#sys.stdin = open("input.txt", "rt")
'''def DFS(L, time, sum):
    global maximum
    if time > m:
        return
    if time==m or (L==n and time <= m):
        if maximum < sum:
            maximum = sum
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                DFS(L+1, time+a[i-1][1], sum+a[i-1][0])
                DFS(L+1, time, sum)
                ch[i]=0


if __name__=="__main__":
    n, m = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(n)]
    ch = [0]*(n+1)
    maximum = 0
    DFS(0,0,0)
    print(maximum)
'''
# 첫시도 20
# 2~5번 time limit

'''def DFS(L, time, sum):
    global maximum
    if time > m:
        return
    if L==n:
        if maximum < sum:
            maximum = sum
    else:
        DFS(L+1, time+a[L-1][1], sum+a[L-1][0])
        DFS(L+1, time, sum)

if __name__=="__main__":
    n, m = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(n)]
    maximum = 0
    DFS(0,0,0)
    print(maximum)'''

# 두번쨰 100

def DFS(L, sum, time):
    global res
    if L==n:
        if sum>res:
            res = sum
    else:
        DFS(L+1, sum+pv[L], time+pt[L])
        DFS(L+1, sum, time)



if __name__=="__main__":
    n, m = map(int,input().split())
    pv = list()
    pt = list()
    for i in range(n):
        a, b = map(int, input().split())
        pv.append(a)
        pt.append(b)
    res = -2147000000
    DFS(0, 0, 0)

# 두가지 상태트리로 뻗는 문제