import sys
from collections import deque
#sys.stdin = open("input.txt", "rt")
n = int(input())
B = [list(map(int, input().split())) for i in range(n)]
H = list(range(min(map(min,B))-1,max(map(max,B))+1))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
maximum = 0
dQ = deque()
for h in H:
    ch = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if ch[i][j] == 0 and B[i][j]>h:
                ch[i][j]=1
                dQ.append((i,j))
                while dQ:
                    now = dQ.popleft()
                    for k in range(4):
                        x = now[0]+dx[k]
                        y = now[1]+dy[k]
                        if 0<=x<n and 0<=y<n and ch[x][y]==0 and B[x][y]>h:
                            ch[x][y]=1
                            dQ.append((x,y))
                cnt+=1
    if maximum < cnt:
        maximum = cnt
print(maximum)

# 첫시도 100 for문이 이렇게 많아도 되는거야?
# 잠길수 있는 모든 경우의수 고려 -> 첫번째 for문
# checklist를 계속 초기화해가면서 경우의수마다 영역 count
# 조건은 지역 높이가 빗물보다 높으면 check하고 주변 탐색


# 격자판 탐색, 특정 영역 문제들은 DFS/BFS 모두 가능

# DFS 풀이
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
sys.setrecursionlimit(10 ** 6) # 재귀 time limit 세팅이 필요함
def DFS(x, y, h):
    ch[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[xx][yy] > h:
            DFS(xx, yy, h)
if __name__ == "__main__":
    n = int(input())
    cnt = 0 # 그럼 이거는 빼도 되는거겠지?
    res = 0
    board = [list(map(int, input().split())) for _ in range(n)]
    for h in range(100):
        ch = [[0] * n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if ch[i][j] == 0 and board[i][j] > h:
                    cnt += 1
                    DFS(i, j, h)
        res = max(res, cnt)
        if cnt == 0:
            break
    print(res)

# 배운점
# 1. 파이썬에서 DFS의 경우 재귀함수 내에 time limit 세팅이 필요함
# 그 세팅 시간 이상이 되면 알아서 종료를 해야 채점이 된다고 함
# 혹시 안되면 sys.setrecursionlimit(10 ** 6) 이 코드를 꼭 추가해야함
