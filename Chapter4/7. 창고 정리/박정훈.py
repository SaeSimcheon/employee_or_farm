import sys

#sys.stdin=open('input.txt','rt')

n = int(input())

begin = list(map(int,input().split()))

m = int(input())

begin.sort()

for _ in range(m):
    begin[0]+=1
    begin[n-1] -= 1
    begin.sort()

print(begin[n-1]-begin[0])
