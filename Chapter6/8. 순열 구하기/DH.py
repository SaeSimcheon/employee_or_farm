'''
순열 구하기
'''

import sys

#sys.stdin = open("in1.txt","r")
n,m = map(int, input().split())

#n,m = 3,2
arr = list(range(1,n+1))

ans = 0

def p(ll,ls):
    global ans
    if len(arr) - len(ll) == m:
        for i in ls:
            print(i,end = " ")
        print()

        ans+=1
        return

    else :
        for i in range(len(ll)):
            p(ll[:i] + ll[i+1:],ls + [ll[i]])


p(arr,[])
print(ans)
