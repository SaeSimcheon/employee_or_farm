'''
랜선자르기(결정알고리즘)
시간

M_l = sum(arr)//m

for i in range(M_l,0,-1):
    if sum([x//i for x in arr]) >= m:
        #print([x//i for x in arr])
        print(i)
        break

M_l = sum(arr)//m

while 1:
    nn = [x//M_l for x in arr]
    
    if sum(nn) >= m:
        print(M_l)
        break
    else:
        aa = [x//(n+1) for x,n in zip(arr,nn)]
        print(aa)
        M_l = max(aa)
'''

import sys

#sys.stdin = open("in3.txt", 'r')


n,m = map(int,input().split())
arr = [int(input()) for i in range(n)]

'''
n,m = 4,11
arr = [802,743,457,539]
'''
lt = 1
rt = max(arr)

ans = 0

while rt >= lt:
    mid = (rt + lt)//2

    S = sum([x//mid for x in arr])

    if S >= m:
        ans = mid
        lt = mid+1
    else:
        rt = mid-1

print(ans)
