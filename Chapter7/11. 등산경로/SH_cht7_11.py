import sys
sys.stdin=open("input.txt", "r")

N = int(input())
seq = [list(map(int,input().split())) for _ in range(N)]

flatten = [x for y in seq for x in y]

min_idx=[flatten.index(min(flatten))//N +1,flatten.index(min(flatten))%N +1]
max_idx=[flatten.index(max(flatten))//N +1,flatten.index(max(flatten))%N +1]

print(min_idx)
print(max_idx)
seq = [[0,*element,0] for element in seq]

add=[0]*(N+2)

seq.insert(0,add)
seq.append(add)

cnt = 0

print(len(seq))
print(len(seq[1]))
print(seq[0])
def DFS(i,j):
    global cnt
    #print(i,j)
    #print(seq[i-1][j])
    if (i ==max_idx[0])&(j == max_idx[1]) :
        cnt +=1
        return 
        
    else:
        
        
    
        if seq[i+1][j] > seq[i][j]:

            DFS(i+1,j)
        
        if seq[i-1][j] > seq[i][j]:
            
            DFS(i-1,j)
            
        if seq[i][j+1] > seq[i][j]:
            
            DFS(i,j+1)
        
        if seq[i][j-1] > seq[i][j]:
            
            DFS(i,j-1)

DFS(min_idx[0],min_idx[1])

print(cnt)

        











