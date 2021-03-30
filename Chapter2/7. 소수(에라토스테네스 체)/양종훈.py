import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())

ch = [0]*(n+1)
cnt=0

for i in range(2, n+1):
    if ch[i]==0:
        cnt += 1
        for j in range(i, n+1, i):
            ch[j] = 1
print(cnt)

'''
n = int(input())

num1 = 0
for i in range(1, n+1):
    num2 = 0
    for j in range(1, i+1):
        if i % j == 0:
            num2 += 1
        if num2 == 3:
            break
    if num2 == 2:
        num1 += 1

print(num1)

'''
