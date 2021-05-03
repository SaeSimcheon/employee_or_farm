'''
수들의 조합
'''

import sys
#sys.stdin = open("in2.txt","r")

_,k = map(int,input().split())
LL = list(map(int,input().split()))
m = int(input())

'''
k = 3
LL = [2,4,5,8,12]
m = 6
'''
num = 0
def DFS(ll,ans,n,m):
    global num
    if n == 0:
        if sum(ans) % m == 0:
            num += 1
    else:
        for i in range(len(ll)):
            DFS(ll[i+1:],ans + [ll[i]],n-1,m)

DFS(LL,[],k,m)
print(num)
