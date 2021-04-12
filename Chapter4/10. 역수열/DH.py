'''
역수열(그리디)
"T" : 빈 공간

'''

import sys

#sys.stdin = open("in1.txt","r")

'''
n = 8
arr = [5,3,4,0,2,1,1,0]
'''

n = int(input())
arr = list(map(int,input().split()))

ans = ["T"] * n

def F(ans,v):
    idx = -1
    n = 0
    while 1:
        idx +=1
        if ans[idx] == "T":
            n+=1

        if n == v+1:
            if ans[idx] == "T":
                return idx
            else:
                continue
for i in range(1,n+1):
    idx = F(ans,arr[i-1])
    ans[idx] = i
for i in ans:
    print(i,end = " ")

