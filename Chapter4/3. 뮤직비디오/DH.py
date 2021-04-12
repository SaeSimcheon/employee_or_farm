'''
뮤직비디오(결정알고리즘)

Sp : 용량이 주어졌을 때 DVD 수

용량 > 가장 긴 노래
'''

import sys

'''
n,m = 9,3
arr = [1,2,3,4,5,6,7,8,9]

'''
#sys.stdin = open('in1.txt',"r")
n,m = map(int,input().split())
arr = list(map(int,input().split()))

lt = max(arr)
rt = sum(arr)

def Sp(arr,v):
    S = 0
    M = 1
    for i in arr:
        if S + i > v:
            S = i
            M += 1
        else:
            S += i
    return M

ans = 0

while rt > lt :

    mid = (rt + lt)//2
    A = Sp(arr,mid)

    if A > m :
        lt = mid + 1

    else :
        rt = mid
        ans = mid
print(ans)


