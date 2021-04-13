import sys
#sys.stdin=open("in5.txt","r")
n=int(input())
base=[list(map(int,input().split())) for _ in range(n)]
ct=0
for i,x in enumerate(base):
    new=base[:i]+base[i+1:]
    c=[True for y in new if x[0]>y[0] or x[1]>y[1] ]
    if sum(c)==len(new):
        ct+=1
        
print(ct)