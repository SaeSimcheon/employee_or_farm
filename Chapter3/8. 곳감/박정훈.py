import sys

#sys.stdin=open('input.txt','rt')

n = int(input())
array1 = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
array2 = [list(map(int, input().split())) for _ in range(m)]

for i in range(m):
    temp = list(range(n))
    if array2[i][1] == 0 :
        temp[0:array2[i][2]+1] = array1[array2[i][0]-1][array2[i][2]:n+1]
        temp[array2[i][2]:n+1] = array1[array2[i][0]-1][0:array2[i][2]+1]
        array1[array2[i][0]-1] = temp
    if array2[i][1] == 1:
        temp[0:array2[i][2]+1] = array1[array2[i][0]-1][array2[i][2]:n+1]
        temp[array2[i][2]:n+1] = array1[array2[i][0]-1][0:array2[i][2]+1]
        array1[array2[i][0]-1] = temp


center_point = n//2
upper = 0
lower = 0
center = array1[center_point][center_point]
for i in range(1,n//2+1):
    upper += sum(array1[center_point-i][center_point-i:center_point+i])
    lower += sum(array1[center_point+i][center_point-i:center_point+i])

print(center+upper+lower)


