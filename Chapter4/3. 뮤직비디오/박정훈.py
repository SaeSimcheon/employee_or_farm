import sys

#sys.stdin=open('input.txt','rt')

n, m = map(int, input().split())

songs = list(map(int, input().split()))

maxx = max(songs)
lt = 1
rt = sum(songs)
mid = (lt+rt)//2

res = 0

def count(capacity):
    cnt = 1
    sum = 0
    for x in songs:
        if mid>=maxx and sum+x > capacity :
            cnt+=1
            sum = x
        else :
            sum+=x
    return cnt

while lt <= rt:
    mid = (lt+rt)//2
    if count(mid) <=m :
        res = mid
        rt = mid-1
    else :
        lt = mid + 1

print(res)
