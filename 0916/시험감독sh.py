import sys
#sys.stdin=open("in5.txt","r")
n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
cnt=n
a=[x-b for x in a]
for x in a:
    while True:
        if x<=0:
            break
        else:
            x-=c
            cnt+=1
print(cnt)
