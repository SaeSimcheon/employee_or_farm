import sys

#sys.stdin=open('input.txt','rt')

n = int(input())
array = list()

for i in range(n):
    l = list(map(int,input().split()))
    array.append(l)


tot = list()
tmp = list()
for i in range(n):
    row = sum(array[i])
    c = list()
    for j in range(n):
        c.append(array[j][i])
        col = sum(c)
    tot.append(max(row,col))

hex1 = list()
for i in range(n):
    hex1.append(array[i][i])

hex2 = list()
for i in range(n):
    hex2.append(array[-i][i])

hex1 = sum(hex1)
hex2 = sum(hex2)

tot.append(max(hex1,hex2))

print(max(tot))

'''
##2차원 리스트
n= int(input())
a = [list(map(int, input().split())) for _ in range(n)]
largest = -2147000000
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1+=a[i][j]
        sum2+=a[j][i]
    if sum1>largest:
        largest=sum1
    if sum2>largest:
        largeset=sum2

sum1 = sum2 = 0
for i in range(n):
    sum1+=a[i][i]
    sum2+=a[-i][i]
if sum1>largest:
    largest=sum1
if sum2>largest:
    largeset=sum2

'''









