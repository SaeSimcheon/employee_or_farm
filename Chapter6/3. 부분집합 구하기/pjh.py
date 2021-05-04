import sys

#sys.stdin=open('input.txt','rt')
'''
def DFS(v,b):
    if v == 4 :
        return
    else :
        if b == True:
            DFS(v+1,True)
            DFS(v+1,False)
            subset = list(range(1,v+1))
            print(subset)
        if b == False:
            DFS(v+1,True)
            DFS(v+1,False)
            subset = list(range(1,v+1))
            subset.pop(v-1)
            print(subset)
'''

def DFS(v):
    if v == n+1:
        for i in range(n+1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else :
        ch[v]=1
        DFS(v+1)
        ch[v]=0
        DFS(v+1)
        
if __name__=="__main__":
    n = int(input())
    ch=[0]*(n+1)
    DFS(1)
