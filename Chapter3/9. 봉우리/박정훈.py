import sys

#sys.stdin=open('input.txt','rt')

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
array1 = [ list( 0 for _ in range(n+2)) for _ in range(n+2) ]

for i in range(n):
    for j in range(n):
        array1[i+1][j+1] = array[i][j]

count = 0
for i in range(n):
    for j in range(n):
        value = array1[i+1][j+1]
        candidate = [array1[i][j+1],array1[i+1][j],array1[i+1][j+2],array1[i+2][j+1]]
        if value > max(candidate):
            count+=1
        candidate = []


print(count)
