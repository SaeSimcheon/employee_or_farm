import sys
from collections import deque
#sys.stdin=open('in1.txt','r')
s,e=map(int,sys.stdin.readline().split())

ch=[0]*10001
ch[s]=1
a=[0]*10001
a[s]=0
d=deque()
d.append(s)

while d:
    x=d.popleft()
    if x==e:
        break
    for i in [-1,1,5]:
        if ch[x+i]==0 and 1<=x+i<=10000:
            d.append(x+i)
            ch[x+i]=1
            a[x+i]=a[x]+1 ## 숫자

print(a[e])


## in2 exit_code뜸
## 거리 1~10000