### 최대 점수 구하기
import sys
#sys.stdin=open('in1.txt','r')
n,m=map(int,sys.stdin.readline().split()) # m : 제한시간

base=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

s=0
def DFS(L,time,score):
    global s
    if time>m:
        return
    if L==n:
        s=max(s,score)    
    else:
        DFS(L+1,time+base[L][1],score+base[L][0])
        DFS(L+1,time,score)


DFS(0,0,0)
print(s)
