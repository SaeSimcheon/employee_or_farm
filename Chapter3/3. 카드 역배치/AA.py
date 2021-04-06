import sys

#sys.stdin=open('input.txt','rt')


n = list(range(1,21))

for i in range(10):
    a, b = map(int,input().split())
    tmp = list()
    for numb in n[a-1:b] :
        tmp.insert(0,numb)
    n[a-1:b] = tmp

print(' '.join(str(numb)  for numb in n ))
