import sys
#sys.stdin = open("input.txt", "rt")
'''def DFS(Dx,Dy):
    global cnt
    if Dx == 6 and Dy == 6:
        cnt += 1
        return
    else:
        for i in range(4):
            x = Dx+dx[i]
            y = Dy+dy[i]
            if 0 <= x <= 6 and 0 <= y <= 6 and a[x][y] == 0:
                a[x][y] = 1
                DFS(x, y)
                a[x][y] = 0

if __name__ == "__main__":
    a = [list(map(int, input().split())) for i in range(7)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0
    a[0][0]=1
    DFS(0,0)
    print(cnt)'''

# 첫시도 100
# 처음에 BFS인줄 알고 준내 안풀리길래 뭔가 했더니 DFS였음
# DFS는 간단하게 할 수 있더라 예전 조합때처럼 DFS뒤에 0으로 바꿔놓으면 OK

# 도착할수 있는 가짓수 문제 -> DFS
# 최단거리를 찾는다면 BFS

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
def DFS(x, y):
    global cnt
    if x==6 and y==6:
        cnt+=1
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<=6 and 0<=yy<=6 and board[xx][yy]==0:
                board[xx][yy]=1
                DFS(xx, yy)
                board[xx][yy]=0

if __name__=="__main__":
    board=[list(map(int, input().split())) for _ in range(7)]
    cnt=0
    board[0][0]=1
    DFS(0, 0)
    print(cnt)

# 배운점
# 1. 격자판 문제에서 경로의 가짓수를 찾으면 DFS, 최단 거리를 찾으면 BFS
# DFS는 깊이 문제, 내려가면서 최적해를 찾는 구조
# BFS는 레벨마다 경우의수를 모두 고려해서 최적해를 찾는 구조