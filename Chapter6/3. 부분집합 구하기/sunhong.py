
import sys
#sys.stdin=open("input.txt", "r")
def DFS(v):
    if v==n+1:
        for i in range(1, n+1):
            if ch[i]==1:
                print(i, end=' ')
        print()
    else:
        ch[v]=1
        DFS(v+1)
        ch[v]=0
        DFS(v+1)

if __name__=="__main__":
    n=int(input())
    ch=[0]*(n+1)
    DFS(1)
    

import sys
from itertools import combinations
#sys.stdin=open('in1.txt')
n=int(sys.stdin.readline())
base=[v for v in range(1,n+1)]
for x in range(1,n+1):
    comb=combinations(base,x)
    for xx in comb:
        for xxx in xx:
            print(xxx,end='')
        print()
## 순서대로안나옴 ##