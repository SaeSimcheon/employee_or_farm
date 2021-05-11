import sys
#sys.stdin = open("input.txt", "rt")
'''def DFS(L,p):
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
'''
# 첫시도 100
# 1번 코드와 비슷한데 다맞네;

# 부분집합 형태 ( O / X )
import sys
sys.stdin=open("input.txt", "r")
def DFS(L, sum):
    global res
    if L==n+1:
        if sum>res:
            res=sum
    else:
        if L+T[L]<=n+1:
            DFS(L+T[L], sum+P[L])
        DFS(L+1, sum)

if __name__=="__main__":
    n=int(input())
    T=list()
    P=list()
    for i in range(n):
        a, b=map(int, input().split())
        T.append(a)
        P.append(b)
    res=-2147000000
    T.insert(0, 0)
    P.insert(0, 0)
    DFS(1, 0)
    print(res)

# 배운점
# 1. 인덱스를 날짜로 보기위해 0을 insert해서 한칸씩 미는 효과를 얻을 수 있음