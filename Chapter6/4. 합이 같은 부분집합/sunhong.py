import sys
#sys.stdin=open('in1.txt','r')
n=int(sys.stdin.readline())
base=list(map(int,sys.stdin.readline().split()))
a=[]
def DFS(x):
    if x==n:
        if sum(a)==sum(base)-sum(a):
            print('YES')
            sys.exit(0)
    else:
        a.append(base[x])
        DFS(x+1)
        a.pop()
        DFS(x+1)
DFS(0)
print('NO')

##야매
import sys
from itertools import combinations
#sys.stdin=open('in5.txt','r')
n=int(sys.stdin.readline())
base=list(map(int,sys.stdin.readline().split()))

cnt=0
for i in range(1,n+1):
    sett=list(combinations(base,i))
    for x in sett:
        if sum(x)==sum(base)/2:
            cnt+=1
if cnt>=1:
    print('YES')
else:
    print('NO')

## return, sys.exit(0) 헷갈리지 말 
