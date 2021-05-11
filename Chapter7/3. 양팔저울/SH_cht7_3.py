import sys

sys.stdin = open("input.txt","rt")

K= int(input())

seq=list(map(int,input().split()))



sum_seq=list(range(1,sum(seq)+1))

#print(sum_seq)

#print(seq)



out = list()
def DFS(L,summ):
    if L == len(seq):
        if (summ <= 0):
            return 
        else:
            out.append(summ)
            return 
    else:
        DFS(L+1,summ+seq[L])
        DFS(L+1,summ-seq[L])
        DFS(L+1,summ)
DFS(0,0)
out=set(out)
print(len(sum_seq)- len(out))
        
        