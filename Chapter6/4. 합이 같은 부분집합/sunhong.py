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

## 재귀함수로 생각을 못해냄