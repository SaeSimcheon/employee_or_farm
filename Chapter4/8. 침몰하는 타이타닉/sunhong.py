import sys
#sys.stdin=open("in5.txt","r")
n,m=map(int,input().split())
weight=list(map(int,input().split()))
weight.sort(reverse=True)

cnt=0
while len(weight)>0:
    if len(weight)==1:
        cnt+=1
        break
    if weight[0]+weight[-1]<=m:
        cnt+=1
        weight=weight[1:-1]
    else:
        cnt+=1
        weight=weight[1:]
print(cnt)

