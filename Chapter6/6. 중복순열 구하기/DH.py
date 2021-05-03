'''
중복순열 구하기
'''
import sys

#sys.stdin = open("in2.txt","r")
n,m = map(int,input().split())
#n,m = 3,2


ll = list(range(1,n+1))
a = 0
def DFS(M,LL):
    global ll,a

    if M == 0:
        for i in LL:
            print(i,end = " ")
        print()
        a += 1
        return

    else:
        for i in ll:
            DFS(M-1,LL+[i])

DFS(m,[])
print(a)
