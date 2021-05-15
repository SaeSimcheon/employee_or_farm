import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    global cnt
    if x == ex and y == ey:
        cnt += 1
    else:
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[xx][yy] > board[x][y]:
                ch[xx][yy] = 1
                DFS(xx, yy)
                ch[xx][yy] = 0


if __name__ == "__main__":
    n = int(input())
    board = [[0]*n for _ in range(n)]
    ch = [[0]*n for _ in range(n)]
    
    max = -2147000000
    min = 2147000000

    ### 답은 입력을 하나하나씩 불러옴과 동시에 최대최소 판단하고 x,y 좌표 구한다음에 하나하나씩 i,j 인덱스 맞춰서 입력
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(n):
            if tmp[j] < min:
                min = tmp[j]
                sx = i
                sy = j
            if tmp[j] > max:
                max = tmp[j]
                ex = i
                ey = j
            board[i][j] = tmp[j]
            
    ch[sx][sy] = 1
    cnt = 0
    DFS(sx, sy)
    print(cnt)



    
'''

## 아니 이것마저 풀어버린다고...?? 100점...
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    global cnt
    if x == mx_x and y == mx_y:
        cnt += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx <= (n-1) and 0 <= yy <= (n-1) and ch[xx][yy] == 0 and mt[xx][yy] > mt[x][y]:
                ch[xx][yy] = 1
                DFS(xx, yy)
                ch[xx][yy] = 0



if __name__ == "__main__":
    n = int(input())
    mt = [list(map(int, input().split())) for _ in range(n)]
    ch = [[0]*n for _ in range(n)]
    cnt = 0
    mx = -2147000000
    mn = 2147000000
    mx_x = 0
    mx_y = 0
    mn_x = 0
    mn_y = 0
    for i in range(n):
        for j in range(n):
            if mt[i][j] < mn:
                mn = mt[i][j]
                mn_x = i
                mn_y = j
            if mt[i][j] > mx:
                mx = mt[i][j]
                mx_x = i
                mx_y = j
    #print(mx_x, mx_y, mx, mn_x, mn_y, mn)
                
    DFS(mn_x, mn_y)
    print(cnt)
    #print(min(mt[0]))
'''
