import sys
#sys.stdin = open("input.txt", "rt")
def DFS(x,y):
    ch[x][y]=1
    if x==9 and ladder[x][y]==1:
        return
    elif x==9 and ladder[x][y]==2:
        print(i)
        sys.exit(0)
    else:
        if y>0 and ladder[x][y-1]==1 and ch[x][y-1]==0:
            DFS(x,y-1)
        elif y<9 and ladder[x][y+1]==1 and ch[x][y+1]==0:
            DFS(x,y+1)
        else:
            DFS(x+1,y)

if __name__=="__main__":
    ladder = [list(map(int, input().split())) for _ in range(10)]
    for i in range(10):
        ch = [[0] * 10 for _ in range(10)]
        if ladder[0][i]==1:
            DFS(0,i)

# 첫시도 100
# 사다리는 좌우 -> 아래로 이동(좌우를 먼저 확인해야함)
# (0,y)마다 확인하면서 아래로 내려오는데, y가 바뀔때마다 check 초기화
# x=9까지 내려왔는데 1이면 다음으로 / 2면 기존에 y좌표 출력하고 종료
# 처음에 생각만 빨리하면 간단하구만

def DFS(x, y):
    ch[x][y]=1
    if x==0:
        print(y)
    else:
        if y-1>=0 and board[x][y-1]==1 and ch[x][y-1]==0:
            DFS(x, y-1)
        elif y+1<10 and board[x][y+1]==1 and ch[x][y+1]==0:
            DFS(x, y+1)
        else:
            DFS(x-1, y)

board=[list(map(int, input().split())) for _ in range(10)]
ch=[[0]*10 for _ in range(10)]
for y in range(10):
    if board[9][y]==2:
        DFS(9, y)

# 도착지점에서 올라가는거는 생각 못했다
# 목표 도착에서 시작하면 경우의수를 다 고려안해도 되서 훨씬 빠름

# 반성점
# 1. 생각의 역발상이 필요할때가 있다
