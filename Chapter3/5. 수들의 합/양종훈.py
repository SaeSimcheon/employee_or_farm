import sys
#sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))

lt = 0
rt = 1
tot = a[0]
cnt = 0

while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1

print(cnt)


'''
n, a = map(int, input().split())
list = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i+1,n+1):
        if sum(list[i:j]) == a:
            cnt += 1
        elif sum(list[i:j]) >= a:
            break
print(cnt)
# time limit 걸려서 60점


n, a = map(int, input().split())
list = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i+1,n+1):
        if sum(list[i:j]) == a:
            cnt += 1
        elif sum(list[i:j]) >= a:
            break
print(cnt)
# time limit 걸려서 40점
'''   