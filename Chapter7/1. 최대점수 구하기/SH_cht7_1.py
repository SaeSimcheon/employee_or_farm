import sys

sys.stdin = open("input.txt","rt")

N,M = map(int,input().split())

mat=[list(map(int,input().split())) for _ in range(N)]
print(mat)
ch = [0]*N

out = 0



def DFS(u):
    global out
    score = sum([mat[idx][0]*v for idx,v in enumerate(ch)])
    time = sum([mat[idx][1]*v for idx,v in enumerate(ch)])
    
    #print(score,time)
    if u == N :
        return 
    if M == time :
        if score >= out:
            out =score
    
    if M < time :
        return
    else:
        ch[u]=1
        DFS(u+1)
        if score >= out:
            out =score
        ch[u]=0
        DFS(u+1)
        if score >= out:
            out =score
DFS(0)
print(out)