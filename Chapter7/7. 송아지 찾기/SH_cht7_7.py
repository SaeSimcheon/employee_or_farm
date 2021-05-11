import sys

sys.stdin = open("input.txt","rt")

S,E= map(int,input().split())

print(S,E)


res = E

def BFS(L,A,B,C,res_):
    print(E)
    print(A,B,C)
    
    res_ = res_ - (S + A*1 - B*1 + C*5) 
    if res_ < 0:
        res_ = E
        
    BFS(L+1,A+1,B,C,res_)  
    BFS(L+1,A,B+1,C,res_)
    BFS(L+1,A,B,C+1,res_)
        
        
BFS(0,0,0,0,res)
