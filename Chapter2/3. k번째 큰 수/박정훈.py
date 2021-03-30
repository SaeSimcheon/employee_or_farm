import random
import itertools
import numpy as np
import sys

#sys.stdin=open('input.txt','rt')

N ,k = map(int,input().split())
select = list(map(int, input().split()))
permut = list(itertools.combinations(select,3))

permut_sum = []
for i in range(len(permut)):
    permut_sum.append(sum(permut[i]))

permut_sum = permut_sum.sort()

new_list = []
for v in permut:
    if v not in new_list:
        new_list.append(v)
new_list.sort(reverse=True)

print(sum(new_list[k]))

'''
import sys
#sys.stdin=open('input.txt','rt')
n,k = map(int,input().split())
a = list(map(int,input().split()))
res = set()
for i in range(n):
    for j in range(i+1,n):
        for m in range(i+2,n):
            res.add(a[i]+a[j]+a[m])
res = list(res)
res.sort(reverse = True)
print(res[k])
'''

