'''
경로 탐색(그래프 DFS)
'''

import sys

#sys.stdin = open("in1.txt","r")
n,m = map(int,input().split())


arr = [[0]*n for i in range(n)]

for i in range(m):
    k,c = map(int,input().split())
    arr[k-1][c-1] = 1

ans = 0
def DFS(s,v,n,arr):
    global ans
    
    if n+1 in v :
#        print(v)
        ans += 1
        return

    else :
        for idx,i in enumerate(arr[s]):
            if i == 1 and idx +1  not in v:
                DFS(idx,v + [idx+1],n,arr)

DFS(0,[1],n-1,arr)
print(ans)
