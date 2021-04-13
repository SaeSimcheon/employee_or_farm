import sys
#sys.stdin=open("c:/Users/jung/Desktop/AA/in1.txt","r")
n,m=map(int,input().split())
base=list(map(int,input().split()))
base.sort()
key=m
start=0
end=len(base)-1
mid=int((start+end)/2)
for _ in range(len(base)):
    if key==base[mid]:
        break
    elif key<base[mid]:
        start=start ## 불필요
        end=mid
        mid=int((start+end)/2)
    else:
        start=mid
        end=end  ## 불필요
        mid=int((start+end)/2)
        
print(mid+1)
