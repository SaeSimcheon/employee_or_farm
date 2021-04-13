import sys

#sys.stdin=open('input.txt','rt')

n, m = map(int,input().split())

numbers = list(map(int,input().split()))

numbers.sort()

print(numbers.index(m)+1)
