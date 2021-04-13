import sys
#sys.stdin=open("in5.txt","r")
k,n=map(int,input().split())
base=[int(input()) for _ in range(k)]


start=1
end=max(base)
max_len=-100
while start<=end:
    mid=(start+end)//2
    nn=0
    for j in range(k):
        nn+=base[j]//mid
    if nn>=n:
        max_len=mid
        start=mid+1
    else:
        end=mid-1
        
print(max_len)



###
#import sys
#sys.stdin=open("c:/Users/jung/Desktop/AA/in1.txt","r")
#k,n=map(int,input().split())
#base=[int(input()) for _ in range(k)]
#max_len=-100
#for i in range(1,max(base)+1):
#    nn=0
#    for j in range(k):
#        nn+=base[j]//i
#    if nn>=n and max_len<i:
#        max_len=i
#print(max_len)

## 시간초과 40점
