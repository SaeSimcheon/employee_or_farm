import sys
#sys.stdin=open('in1.txt','r')
n=int(sys.stdin.readline())
base=list(map(int,sys.stdin.readline().split()))

dy=[0]*n
dy[0]=1

for i in range(1,n):
    len=0
    for j in range(0,i):
        if base[i]>base[j]:
            len=max(len,dy[j]+1)
    dy[i]=max(1,len)
    
print(max(dy))

## 4번이랑 걍 완전히 같은 문제