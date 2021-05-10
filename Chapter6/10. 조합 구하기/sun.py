import sys
#sys.stdin=open('in1.txt','r')
n,m=map(int,sys.stdin.readline().split())

def DFS(L,d):
    global cnt
    if L==m :#and sorted(a)==a and len(a)==m:
        cnt+=1
        for x in a:
            print(x,end=' ')
        print()
    else:
        for i in range(d,n+1):
            a[L]=i
            DFS(L+1,i+1) ## i+1자리에 d+1넣어서 헤맸음

a=[0]*m
cnt=0
DFS(0,1)
print(cnt)

##야매
import sys
from itertools import combinations
#sys.stdin=open('in1.txt','r')
n,m=map(int,sys.stdin.readline().split())
base=list(range(1,n+1))
comb=list(combinations(base,m))
for x in comb:
    for y in x:
        print(y,end=' ')
    print()
print(len(list(combinations(base,m))))

            
