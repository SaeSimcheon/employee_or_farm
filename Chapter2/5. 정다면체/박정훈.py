import sys
from collections import Counter

#sys.stdin=open('input.txt','rt')

N,M = map(int, input().split())

sums = list()
for i in range(1,N+1):
    for j in range(1,M+1):
        sum = i+j
        sums.append(sum)

result = Counter(sums)
counts = list()
keys = list()
for key in result:
    counts.append(result[key])
for key in result:
    keys.append(key)

tmp=counts[0]

for i in range(1,len(counts)):
    if tmp < counts[i]:
        tmp = counts[i]
        index = list()
        index.append(i)
    if tmp == counts[i]:
        index.append(i)

print(sort(counts[index]) for index in index)

'''
import sys
sys.stdin = open('input.txt','r')
n,m = map(int, input().split())
cnt = [0]*(n+m+3)
for i in range(1,n+1):
    for j in range(1,m+1):
        cnt[i+j]+=1
max = -2147000000
for i in range(0,n+m+1):
    if cnt[i] > max :
        max = cnt[i]
for i in range(len(cnt)):
    if cnt[i] == max :
        print(i, end=' ')
'''

