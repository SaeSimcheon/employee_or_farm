import sys
from itertools import combinations
#sys.stdin=open("in1.txt", "r")/sys.stdin.readline()
n, k=map(int, sys.stdin.readline().split())
a=list(map(int, sys.stdin.readline().split()))
m=int(sys.stdin.readline())
cnt=0
for x in combinations(a, k):
    if sum(x)%m==0:
        cnt+=1
print(cnt)


