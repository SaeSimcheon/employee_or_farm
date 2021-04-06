import sys

#sys.stdin=open('input.txt','rt')

n = int(input())

for i in range(n):
    chr = str(input()).lower()
    tmp = str()
    for j in chr:
        tmp = j + tmp
        tmp = tmp.lower()
    if chr == tmp:
        print('#%d' % (i+1),'YES', end='\n')
    else :
        print('#%d' % (i+1),'NO',end='\n')




