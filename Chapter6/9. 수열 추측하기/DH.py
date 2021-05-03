'''
수열 추측하기
'''

import sys
from itertools import permutations
#sys.stdin = open("in5.txt","r")

n,f = map(int,input().split())
ll = list(range(1,n+1))


def Sum(ls):
    while len(ls) != 1:
        ls = [ls[x]+ls[x+1]for x in range(len(ls)-1)]

    return ls[0]


for i in list(permutations(ll)):
    if Sum(i) == f:
        for nn in i:
            print(nn,end = " ")
        
        print()
        break
