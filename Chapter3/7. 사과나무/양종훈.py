import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

res = 0
s = e = n//2
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(res)


'''
n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]

#print(mat[0][-0:])
apple = 0
for i in range(n):
    if i == n//2:
        apple += sum(mat[i])
    else:
        j = abs(n//2 - i)
        apple += sum(mat[i][j:-j])
print(apple)
'''