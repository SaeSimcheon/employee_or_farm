import sys

#sys.stdin=open('input.txt','rt')

n, m = map(int, input().split())

station = list()

for _ in range(n):
    station.append(int(input()))

station.sort()
#print(station)
def count(distance):
    cnt = 1
    place = station[0]
    for i in range(n-1) :
        if station[i+1]- place >= distance:
            cnt+=1
            place = station[i+1]
        else :
            cnt = cnt
    return cnt

lt = min(station)
rt = max(station)

res = 0

while lt <= rt:
    mid = (lt+rt)//2
    if count(mid) >= m :
        lt = mid +1
        res = mid
    else :
        rt = mid-1

print(res)
