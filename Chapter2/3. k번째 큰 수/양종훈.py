import sys
#sys.stdin = open("input.txt", "rt")

import itertools

n, k = map(int, input().split())
arr = list(map(int, input().split()))

nCr = itertools.combinations(arr, 3)
#print(list(nCr))

a = []
for i in list(nCr):
    b = sum(i)
    #print(b)
    a.append(b)
a = list(set(a))
a.sort(reverse=True)
print(a[k-1])
