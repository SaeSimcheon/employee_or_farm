import sys

sys.stdin = open("input.txt","rt")

N= int(input())

seq=[ int(input()) for _ in range(N)]

out = 2000000000
def DFS(L,A ,B , C):
    global out
    #print(L)
    
    if L == N:
        if (A == B) |(A == C) |(B == C):
            return
        if out >= max([A,B,C])-min([A,B,C]):
            print(L,out)
            out = max([A,B,C])-min([A,B,C])
            print(out)
    else:
        DFS(L+1,A+seq[L],B,C)
        DFS(L+1,A,B+seq[L],C)
        DFS(L+1,A,B,C +seq[L])
        


DFS(0,0,0,0)
print(out)