import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())

res = 0
s = 0
e = n-1
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(res)
'''
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
#b = [list(map(int, input().split())) for _ in range(n)]

for _ in range(m):
    c, x, d = map(int, input().split())
    if x == 0:
        a[c-1] = a[c-1][d:] + a[c-1][:d]
    else:
        a[c-1] = a[c-1][n-d:] + a[c-1][:n-d]
#print(a)

s = 0
e = n
gam = 0
for i in range(n):
    for j in range(s, e):
        gam += a[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(gam)
# 이거 3,4 번만 틀리는데 왜 그런지 모르겠음...
'''