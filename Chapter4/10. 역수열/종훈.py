import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)

seq = [0] * n

for i in range(1, n+1):
    for j in range(n):
        if a[i] == 0 and seq[j] == 0:
            seq[j] = i + 1
            break
        elif seq[j] == 0:
            a[i] -= 1
for x in seq:
    print(x, end = " ")


'''
n = int(input())
a = list(map(int, input().split()))

res = [0] * n

for i in range(n):
    cnt = 0
    
    for j in range(n):
        if cnt == a[i]:
            res[j] = i+1
            break
        if res[j] == 0:
            cnt += 1

for i in range(n):
    print(res[i], end = " ")
'''     