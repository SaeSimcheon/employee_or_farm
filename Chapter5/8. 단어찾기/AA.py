import sys

#sys.stdin=open('input.txt','rt')

n = int(input())

word = dict()

for i in range(n):
    w = input()
    word[w] = 1

for i in range(n-1):
    w = input()
    word[w]=0

for key, val in word.items():
    if val == 1:
        print(key)
    



