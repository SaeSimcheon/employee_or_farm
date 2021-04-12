'''
씨름 선수(그리디)

이중 for 문 사용했는데 별로 인가보네;;(100점 나오긴 함)


답 : 키로 정렬(reverse) >> 큰 몸무게 나오면 cnt += 1
'''

import sys

#sys.stdin = open("in1.txt","r")

'''
n = 5
arr = [[172,67],[183,65],[180,70],[170,72],[181,60]]
'''


n = int(input())
arr = [list(map(int,input().split())) for x in range(n)]

Re = sum([any([all([x[0] > A[0],x[1] > A[1]]) for x in arr])for A in arr])

print(n - Re)

