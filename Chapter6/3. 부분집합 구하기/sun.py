import sys
#sys.stdin=open('in1.txt','r')
n=int(sys.stdin.readline())

a=[]
def DFS(x):
    if x==n+1:
        for xx in a:
            print(xx, end=' ')
        print()
    else:
        a.append(x)
        DFS(x+1)
        a.pop()
        DFS(x+1)

DFS(1)
