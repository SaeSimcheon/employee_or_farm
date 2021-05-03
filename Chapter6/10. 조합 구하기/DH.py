'''
조합 구하기
'''

import sys
#sys.stdin = open("in2.txt","r")

n,m = map(int,input().split())
#n,m = 4,2

LL = list(range(1,n+1))
#print(LL)
num = 0
def DFS(ll,ans,n):
    global num
    if n == 0:
        for i in ans:
            print(i, end = " ")
        print()
        num += 1
    else:
        for i in range(len(ll)):
            DFS(ll[i+1:],ans + [ll[i]],n-1)

DFS(LL,[],m)
print(num)
