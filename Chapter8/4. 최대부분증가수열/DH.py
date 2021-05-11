'''
최대 부분 증가수열
'''

import sys

#sys.stdin = open("in2.txt")

n = int(input())
arr = list(map(int,input().split()))
#print(arr)
'''
n = 8
arr = [5,3,7,8,6,2,9,4]
'''
dy = [1] + [0] * (n-1)

for i in range(1,n):
    tmp_m = 0
    tmp_v = arr[i]
    for ls,dyy in zip(arr[:i],dy[:i]):
        if ls < tmp_v:
            if tmp_m < dyy:
                tmp_m = dyy
    dy[i] = tmp_m + 1
print(max(dy))
