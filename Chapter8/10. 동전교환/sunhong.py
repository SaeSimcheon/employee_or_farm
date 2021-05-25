import sys
#sys.stdin=open('in1.txt','r')
n=int(sys.stdin.readline())
base=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())

dy=[24700000]*(m+1)
dy[0]=0
for i in range(n):
    w=base[i]
    for j in range(w,m+1):
        dy[j]=min(dy[j],dy[j-w]+1)

print(dy[-1])
