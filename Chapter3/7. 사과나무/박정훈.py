import sys

#sys.stdin=open('input.txt','rt')

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

center_point = n//2
upper = 0
lower = 0
center = sum(array[n//2])
for i in range(1,n//2+1):
    upper += sum(array[center_point-i][i:-i])
    lower += sum(array[center_point+i][i:-i])

print(center+upper+lower)


'''

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = 0

s = e = n//2
for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]

    if i<n//2:
        s-=1
        e+=1
    else :
        s+=1
        e-=1


'''
