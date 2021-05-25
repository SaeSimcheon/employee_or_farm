import sys
#sys.stdin=open('in1.txt','r')
n,c=map(int,sys.stdin.readline().split())
w=[]
v=[]
for _ in range(n):
    ww,vv=map(int,sys.stdin.readline().split())
    w.append(ww)
    v.append(vv)

dy=[0]*(c+1)

for i in range(n):
    weight=w[i]
    value=v[i]
    for j in range(weight,len(dy)):
        dy[j]=max(dy[j],dy[j-weight]+value)

print(dy[-1])
