import sys
#sys.stdin=open("in5.txt","r")
l=int(input())
base=list(map(int,input().split()))
m=int(input())
base.sort()

for _ in range(m):
    base=[base[0]+1]+base[1:-1]+[base[-1]-1]
    base.sort()
    
print(base[-1]-base[0])
