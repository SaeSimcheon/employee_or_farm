import sys

#sys.stdin=open('input.txt','rt')

n = str(input())
numb = str()

for i in n:
    if i.isdecimal():
        numb = numb+i


numb = int(numb)

yak = list()

for i in range(1,numb+1):
    if numb % i == 0:
        yak.append(i)

print(numb)
print(len(yak))




