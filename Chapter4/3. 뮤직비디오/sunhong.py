import sys
#sys.stdin=open("in1.txt","r")
n,m=map(int,input().split())
base=list(map(int,input().split()))

def capa(capa):
    cnt=1
    sum=0
    for x in base:
        if sum+x>capa:
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt

start=min(base)
end=sum(base)
res=end ### 작을 수록 좋아지는거
while start<=end:
    mid=(start+end)//2
    if capa(mid)<=m:
        end=mid-1
        if mid<res:
            res=mid
    else:
        start=mid+1
        
print(res)
