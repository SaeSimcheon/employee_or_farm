import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

largest = -2147000000
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

# 대각선 합
sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

print(largest)




'''
n = int(input())

mat = []
for i in range(n):
    row = list(map(int, input().split()))
    mat.append(row)

tot_sum = []
diag_sum1 = 0
diag_sum2 = 0
for i in range(n):
    row_sum = sum(mat[i])
    tot_sum.append(row_sum)

    diag_sum1 += mat[i][i]
    diag_sum2 += mat[i][n-i-1]

    col_sum = 0
    for j in range(n):
        col_sum += mat[j][i]
    tot_sum.append(col_sum)
    
tot_sum.append(diag_sum1)
tot_sum.append(diag_sum2)

print(max(tot_sum))
'''