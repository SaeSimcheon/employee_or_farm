'''
동전 바꿔주기
'''

import sys

#sys.stdin = open("in1.txt","r")

t = int(input())
k = int(input())

arr = []

for i in range(k):
    p,n = map(int,input().split())
    arr.append([p,n])


ans = 0
def DFS(ls,s,T):
    global ans

    if T >= t or k == s:
        if T == t:
            ans += 1
        return
    else:
        for num in range(ls[s][1]+1):
            DFS(ls,s+1,T+num*ls[s][0])
DFS(arr,0,0)
print(ans)

    
