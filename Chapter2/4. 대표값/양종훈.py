import sys
#sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())

import collections

li = []
for i in range(1, n+1):
    for j in range(1, m+1):
        a = i+j
        li.append(a)

cnt = collections.Counter(li)

#print([k for k,v in cnt.items() if max(cnt.values()) == v])
for k, v in cnt.items():
    if max(cnt.values()) == v:
        print(k)

'''
n, m = map(int, input().split())

cnt = [0]*(n+m+3)

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1
'''