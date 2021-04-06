import sys

#sys.stdin=open('input.txt','rt')

a, b = map(int, input().split())
c = list(map(int,input().split()))

count = 0
for i in range(0,a):
    if c[i] == b:
        count += 1
    tmp = 0
    for j in range(i,a+1):
        tmp += sum(c[i:j+1])
        if tmp == b:
            count += 1

print(count)
