import sys
#sys.stdin = open('input.txt','r')
'''def DFS(L,k,v):
    global res
    if k>limit:
        return
    if k==limit:
        if res<v:
            res=v
    else:
        #print(k,v)
        for i in range(n):
            DFS(L+1,k+a[i][0],v+a[i][1])

n, limit = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
res = 0
DFS(0,0,0)
print(res)'''

# 첫시도 40
# 냅색 알고리즘이 뭐야? 강의 안보고 DFS로 해봤는데 3~5번 time limit

n, limit = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
dy = [0]*(limit+1)
for i in range(n):
    for j in range(limit+1):
        if a[i][0]<=j:
            if dy[j-a[i][0]]+a[i][1]>dy[j]:
                dy[j] = dy[j-a[i][0]]+a[i][1]
            #print(dy)
print(max(dy))

# 두번째 100 - DP로 풀이
# 강의 앞부분 보고 풀었음