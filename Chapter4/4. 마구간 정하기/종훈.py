import sys
#sys.stdin = open("input.txt", "rt")

n, c = map(int, input().split())
Line = []

for _ in range(n):
    tmp = int(input())
    Line.append(tmp)
Line.sort()

lt = 1
rt = Line[n-1]

def Count(len):
    cnt = 1
    ep = Line[0]
    for i in range(1, n):
        if Line[i] - ep >= len:
            cnt += 1
            ep = Line[i]
    return cnt

while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid -1
print(res)

'''
# 결국 이거 못풀었음...ㅠㅠ

n, c = map(int, input().split())

home = []
for i in range(n):
    home.append(int(input()))

#print(home)
home.sort()
lt = min(home)
rt = max(home)
#print(home)
def stay(x):
    cnt = 1
    for i in range(1, n):
        if home[i] - home[i-1] >= x:
            cnt += 1
    return cnt

#print(stay(3))

while lt <= rt:
    mid = (lt+rt)//2
    res = mid
    if stay(mid) < c:
        rt = mid + 1
    else:
        lt = mid - 1

print(res)

'''