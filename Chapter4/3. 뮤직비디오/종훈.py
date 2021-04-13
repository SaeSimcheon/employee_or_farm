import sys
#sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
Music = list(map(int, input().split()))

lt = 1
rt = sum(Music)
res = 0

def Count(capacity):
    cnt = 1
    sum = 0
    for x in Music:
        if sum + x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt

maxx = max(Music)

while lt <= rt:
    mid = (lt+rt)//2
    if mid >= maxx and Count(mid) <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(res)


'''
n, m = map(int, input().split())
song = list(map(int, input().split()))


lt = 1
rt = sum(song)

def Count(x):
    cnt = 1
    size = 0
    for i in range(n):
        size += song[i]
        if size > x:
            size = song[i]
            cnt += 1
    return cnt

res = 0
while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(res)
'''

'''
n, m = map(int, input().split())
song = list(map(int, input().split()))

lt = n//m
rt = 2*n//m
#print(lt, rt)

a, b, c = 2147000000, 2147000000, 2147000000

while True:
    
    res1 = max(a, b, c)
    a = sum(song[:lt])
    b = sum(song[lt:rt])
    c = sum(song[rt:])
    res = max(a, b, c)
    if min(a, b, c) == a:
        lt += 1
    elif min(a, b, c) == c:
        rt += 1
    elif min(a, b, c) == b and max(a, b, c) == a:
        lt -= 1
    else:
        rt += 1

    if res1 < res:
        break
print(res1)
# 시간제한 및 오답으로 20점...
'''
