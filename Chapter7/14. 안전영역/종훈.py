import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 


# 재귀함수 횟수제한 늘려주기
sys.setrecursionlimit(10**6)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y, h):
    ch[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and board[xx][yy] > h and ch[xx][yy] == 0:
            DFS(xx, yy, h)


if __name__ == "__main__":
    n = int(input())
    res = 0
    board = [list(map(int, input().split())) for _ in range(n)]
    for h in range(100):
        ch = [[0]*n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if ch[i][j] == 0 and board[i][j] > h:
                    cnt += 1
                    DFS(i, j, h)
        res = max(res, cnt)
        if cnt == 0: # board에서 max구하지 않고 뒤에 for문 안돌게 하는 방법
            break
    print(res)


'''
# 이거하면 100점
# default값으로 설정되어 있는 재귀 호출 횟수(약 1000번?)을 넘어서면 에러가 발생한다.
# 재귀 호출 횟수를 늘려주는 것
import sys
sys.setrecursionlimit(10**7)


# 지금 60점
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y, rain):
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and board[xx][yy] > rain and ch[xx][yy] == 0:
            
            ch[xx][yy] = 1
            DFS(xx, yy, rain)


if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    #print(board)
    
    mx = -2147000000
    for i in range(n): # 나는 맥스 구해서 1부터 맥스까지만 검사
        for j in range(n):
            if board[i][j] > mx:
                mx = board[i][j]
    #print(mx)
    res = -2147000000
    for k in range(1, mx):
        ch = [[0]*n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if board[i][j] > k and ch[i][j] == 0:
                    cnt += 1
                    ch[i][j] = 1
                    DFS(i, j, k)
        if cnt > res:
            res = cnt
    print(res)
'''            
    
