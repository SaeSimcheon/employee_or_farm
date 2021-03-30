'''
정다면체
'''
import sys
from collections import Counter
#sys.stdin = open("in1.txt","rt")


N,M = map(int,input().split())

#print(N,M)
RE = [n+m for n in range(1,N+1) for m in range(1,M+1)]
RE = Counter(RE)


MM = max(RE.values())

for k,v in RE.items():
    if v == MM:
        print(k,end = " ")
