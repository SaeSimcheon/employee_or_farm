import sys
#sys.stdin = open("input.txt", "rt")
def DFS(v):
    global cnt
    if v==n:
        cnt += 1
    else:
        for i in range(1,n+1):
            if adj[v][i]==1 and ch[i]==0:
                ch[i]=1
                DFS(i)
                ch[i]=0

if __name__=="__main__":
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(m)]
    adj = [[0] * (n+1) for _ in range(n+1)]
    for j in a:
        ni, nj = j
        adj[ni][nj] = 1
    ch = [0]*(n+1)
    ch[1] = 1
    cnt = 0
    DFS(1)
    print(cnt)

# 반성점
# 1. 비슷하게 접근했지만 check 하는걸 생각을 못했음

# 배운점
# 1. 수열 풀이와 유사하게 check가 필요(한번 방문한 노드는 다시 방문X)
# 2. 상태트리 구현할떄 좀더 생각하고 할 필요가 있어보임