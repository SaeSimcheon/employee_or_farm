import sys
#sys.stdin = open("input.txt", "rt")
'''def DFS(v, summ):
    global maximum
    if summ > c:
        return
    if v == n:
        if summ > maximum and summ <= c:
            maximum = summ
    else:
        DFS(v+1, summ+a[v])
        DFS(v+1, summ)
if __name__  ==  "__main__":
    c, n = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    maximum = 0
    DFS(0, 0)
    print(maximum)'''

# 첫시도 80
# 5번문제 time limit 개오래걸린다 해결방법을 모르겠네
from collections import deque
def DFS(L, sum, tsum):
    global result
    if sum+(total-tsum)<result: # 앞으로 판단해야할 무게들 + 기존에 더한 무게
        return
    if sum>c:
        return
    if L==n:
        if sum>result:
            result=sum
    else:
        DFS(L+1, sum+a[L], tsum+a[L])
        DFS(L+1, sum, tsum+a[L])

if __name__  ==  "__main__":
    c, n = map(int, input().split())
    a = [0]*n
    result = -247000000
    for i in range(n):
        a[i]=int(input())
    total=sum(a)
    DFS(0,0,0)
    print(result)

# 느낀점
# 1. 상태트리는 모든 경우의수를 고려하지만, 속도를 위해 cutoff가 필요
# 그거를 잘 고려해봐야할듯

# 배운점
# 1. 상태트리의 합 문제에서 기준 정답이 있을때, 현재까지 합산된 것과 이후에 합산될 거도 같이 고려하면 연산을 덜할수 있음