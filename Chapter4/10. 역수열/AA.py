import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n,0,-1):
    b.insert(a[i-1],n)
    n-=1
    #print(b)
for j in b:
    print(j, end=' ')
