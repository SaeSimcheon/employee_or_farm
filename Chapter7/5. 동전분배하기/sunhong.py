## 세 명에게 n개의 동전을 총액편차가 제일 작게 분배, 최소차를 출력
import sys
from collections import Counter 
#sys.stdin=open('in1.txt','r')
n=int(sys.stdin.readline())
base=[int(sys.stdin.readline()) for _ in range(n)]

result=247000000000
a=[0]*3
def DFS(L):
    global result
    if L==n:
        dif=max(a)-min(a)
        if len(Counter(a))==3: #
            result=min(dif,result)
    else:
        for i in range(3):
            a[i]+=base[L]
            DFS(L+1)
            a[i]-=base[L]

DFS(0)
print(result)
