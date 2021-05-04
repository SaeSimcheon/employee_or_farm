import sys
#sys.stdin = open("input.txt", "rt")
'''
def DFS(L,res):
    global cnt
    if res>m:
        return
    if res==m:
        cnt.append(L)
    else:
        for i in range(n):
            DFS(L+1,res+a[i])

if __name__=="__main__":
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    cnt = []
    DFS(0,0)
    print(min(cnt))

# 첫시도 40 / 3~5번 time limit

def DFS(L,res):
    global cnt
    if res > m:
        return
    if cnt < L:
        return
    if res == m:
        if L < cnt:
            cnt = L
    else:
        for i in range(n):
            DFS(L+1,res+a[i])

if __name__=="__main__":
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    a.sort(reverse=True)
    cnt = 2147000000
    DFS(0,0)
    print(cnt)
# 두번째 100
# 강의 앞부분 보고 다시 풀었음
# 내림차순 + 기존보다 큰 count면 return
'''

def DFS(L,sum):
    global res
    if L>res:
        return
    if sum>m:
        return
    if sum==m:
        if L<res:
            res=L
    else:
        for i in range(n):
            DFS(L+1, sum+a[i])

if __name__=="__main__":
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    res = 2147000000
    a.sort(reverse=True)
    DFS(0,0)
    print(res)

# 배운점
# 1. cutoff 기준 / 최소값을 찾을 때 정렬