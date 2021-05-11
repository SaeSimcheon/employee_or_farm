import sys

sys.stdin = open("input.txt","rt")

N = int(input())
seq1=list()
seq2=list()

for _ in range(N):
    s1,s2=map(int,input().split()) 
    seq1.append(s1)
    seq2.append(s2)



res = 0

def DFS(time, out):
    global  res

    if time > N :
        return
    if time == N :
        if res <=out:
            res = out
        
    else:
        DFS(time +seq1[time] ,out +seq2[time])
        DFS(time+1,out)
        
DFS(0,0)
print(res)