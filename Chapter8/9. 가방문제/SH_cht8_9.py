import sys
sys.stdin = open("input.txt","rt")

N ,M = map(int,input().split())
seq=[list(map(int,input().split())) for _ in range(N)]

print(seq)


        
    
ch=[0]*N
col=list(zip(*seq))
column = list(col[0])
value = list(col[1])
out = list()

def DFS(W):
    if W < 0:
        return
    if min(column) > W >=0:
        print(W)
        print(ch)
        out.append(sum([i*value[idx] for idx,i in enumerate(ch)]))
        return 
    else:
        for i in range(N):
            ch[i]+=1
            DFS(W - column[i])
            ch[i]-=1
            

DFS(M)
print(max(out))


#print(ch)