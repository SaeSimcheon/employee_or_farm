import sys
#sys.stdin = open("input.txt", "rt")
'''def DFS(L, s):
    global cnt
    if L==k:
        if sum(res[:k])%m==0:
            cnt+=1
    else:
        for i in range(s,n+1):
            res[L] = a[i-1]
            DFS(L+1, i+1)

if __name__=="__main__":
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    m = int(input())
    res=[0]*n
    cnt = 0
    DFS(0, 1)
    print(cnt)'''

# 첫시도 100
# 이전 문제에 배운 조합을 활용하면 쉽게 풀수 있음
def DFS(L, s, sum):
    global cnt
    if L == k:
        if sum%m==0:
            cnt+=1
    else:
        for i in range(s, n):
            DFS(L+1, i+1, sum+a[i])

if __name__=="__main__":
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    m = int(input())
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)
# 배운점
# 1. 더하는 과정도 DFS로 처리하면 저장하는 벡터를 만들 필요가 없다

# itertools를 이용한 풀이 / 재귀함수를 이용해서 구하는게 기본!

import sys
import itertools as it
sys.stdin = open("input.txt","rt")
n, k = map(int,input().split())
a = list(map(int,input().split()))
m = int(input())
cnt = 0
for x in it.combinations(a, k):
    if sum(x)%m==0:
        cnt+=1
print(cnt)