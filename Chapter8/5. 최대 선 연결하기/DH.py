'''
최대 선 연결하기
'''

import sys

#sys.stdin = open("in1.txt")
n = int(input())
arr = list(map(int,input().split()))
'''

n = 10
arr = [4,1,2,3,9,7,5,6,10,8]
'''
dy = [(1,arr.index(1))]

ans = 0
for i in range(2,n+1):

    tmp_i = arr.index(i)

    tmp_m = 0

    for i in dy:

        if i[1] < tmp_i:
            if tmp_m < i[0]:
                tmp_m = i[0]

    dy.append((tmp_m+1,tmp_i))

    if ans < dy[-1][0]:
        ans = dy[-1][0]
print(ans)

