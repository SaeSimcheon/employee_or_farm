'''
자리수 합
'''
import sys

#sys.stdin = open("in1.txt","rt")


def degit_sum(x):
    x = str(x)
    x = list(x)
    return sum([int(i) for i in x])

_ = input()
L = list(map(int,input().split()))


L = [[idx,degit_sum(i),i] for idx,i in enumerate(L)]
L = sorted(L, key = lambda x:(-x[1],x[0]))
print(L[0][2])
'''
for i in L:
    print(i,degit_sum(i))
'''

