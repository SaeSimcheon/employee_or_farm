import sys
#sys.stdin = open("input.txt", "rt")
'''def DFS(Dx,Dy):
    global cnt
    if Dx == end[0] and Dy == end[1]:
        cnt += 1
        return
    else:
        for i in range(4):
            x = Dx+dx[i]
            y = Dy+dy[i]
            if 0 <= x <= n-1 and 0 <= y <= n-1 and ch[x][y] == 0 and a[Dx][Dy] < a[x][y]:
                ch[x][y] = 1
                DFS(x, y)
                ch[x][y] = 0

if __name__ == "__main__":
    n = int(input())
    a = [list(map(int, input().split())) for i in range(n)]
    start = [[i,j] for i in range(n) for j in range(n) if a[i][j] == min(min(a))][0]
    end = [[i,j] for i in range(n) for j in range(n) if a[i][j] == max(max(a))][0]
    ch = [[0]*n for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    ch[start[0]][start[1]]=1
    cnt = 0
    DFS(start[0],start[1])
    print(cnt)'''

# 첫시도 60
# 2,4번 답이 틀렸대

'''def DFS(Dx,Dy):
    global cnt
    if Dx == end[0] and Dy == end[1]:
        cnt += 1
        return
    else:
        for i in range(4):
            x = Dx+dx[i]
            y = Dy+dy[i]
            #print(a[x][y])
            if 0 <= x <= n-1 and 0 <= y <= n-1 and ch[x][y] == 0 and a[Dx][Dy] < a[x][y]:
                ch[x][y] = 1
                DFS(x, y)
                ch[x][y] = 0

if __name__ == "__main__":
    n = int(input())
    a = [list(map(int, input().split())) for i in range(n)]
    start = [[i,j] for i in range(n) for j in range(n) if a[i][j] == min(map(min,a))][0]
    end = [[i,j] for i in range(n) for j in range(n) if a[i][j] == max(map(max,a))][0]
    ch = [[0]*n for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    ch[start[0]][start[1]]=1
    cnt = 0
    DFS(start[0],start[1])
    print(cnt)'''

# 두번째 100
# 왜일까 찾아보니 start랑 end 포인트를 잘못 잡더라
# 2차원 리스트에서 min(list)는 원소 리스트의 합이 최소인걸 찾음
# 그래서 map 함수를 써서,, min(map(min, list)) 이런식으로 하면 리스트 원소가 최소인걸 찾음

# 가장 낮은곳과 높은곳이 달라질수 있다는걸 생각해야함
# 이전 문제와 마찬가지로 경로 가짓수를 찾는거라 DFS

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def DFS(x, y):
    global cnt
    if x==ex and y==ey:
        cnt+=1
    else:
        for k in range(4):
            xx=x+dx[k]
            yy=y+dy[k]
            if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>board[x][y]:
                ch[xx][yy]=1
                DFS(xx, yy)
                ch[xx][yy]=0

if __name__=="__main__":
    n=int(input())
    board=[[0]*n for _ in range(n)]
    ch=[[0]*n for _ in range(n)]
    max=-2147000000
    min=2147000000
    for i in range(n):
        tmp=list(map(int, input().split()))
        for j in range(n):
            if tmp[j]<min:
                min=tmp[j]
                sx=i
                sy=j
            if tmp[j]>max:
                max=tmp[j]
                ex=i
                ey=j
            board[i][j]=tmp[j]
    ch[sx][sy]=1
    cnt=0
    DFS(sx, sy)
    print(cnt)

# 배운점
# 1. 이차원 리스트에서 min(list)는 원소 리스트들의 합의 최소를 찾음, 그래서 min(min(list))는 원소로 반환이 안됨
# 그래서 행렬에서 최소 원소를 찾으려면 min(map(min,list)) 이런식으로 map을 활용해야함
