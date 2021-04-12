'''
이분검색

import sys

#sys.stdin = open("in1.txt", 'r')

n,m = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort()
print(arr.index(m)+1)
'''


import sys

#sys.stdin = open("in1.txt", 'r')

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

lt = 0
rt = n

while 1:
    mid = (lt+rt)//2
    if arr[mid] == m:
        print(mid+1)
        break
    else:
        if arr[mid] > m:
            rt = mid
        else:
            lt = mid


