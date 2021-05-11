import sys

sys.stdin = open("input.txt","rt")

T= int(input())
k= int(input())

seq=[list(map(int,input().split())) for _ in range(k)]


count= 0 

def DFS(L,stack):
    global count
    
    if stack > T:
        return
    if L == k:
        if stack == T :
            count +=1
    else:
        for add in range(seq[L][1]+1):
            
            DFS(L+1,stack + seq[L][0]*add)

            
DFS(0,0)
print(count)
        
    