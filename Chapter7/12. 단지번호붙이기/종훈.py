import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 


############### 질문!!
# 정답코드에서 board 부를 때 왜
# invalid literal for int() with base 10: '\n'
# 나오는지 아는 사람..?



dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 역시 DFS에서 무조건 if else문 있어야 하지는 않네
def DFS(x, y):
    global cnt
    cnt += 1
    board[x][y] = 0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and board[xx][yy] == 1:
            DFS(xx, yy)
    


if __name__ == "__main__":
    n = int(input())
    # 다 붙어 있어서 띄워주려고 str로 input받고 for문 써서 하나씩 따로 입력했는데 split()만 안하면 되는 거 였음..
    board = [list(map(int, input())) for _ in range(n)]
    res = []
    # 난 cnt를 밖에서 지정해주고 DFS 끝날 때마다 0으로 초기화 시켰는데 여긴 시작할 때 안에서 0으로 만드니까 더 간단
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cnt = 0
                DFS(i, j)
                res.append(cnt)

    print(len(res))
    res.sort()  
    for x in res:
        print(x)


'''
# 설명듣고 풀어서 100점
# 근데 DFS에 IF문에 조건 없어도 될 듯한데 답지 봐야지

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    global cnt
    if board[x][y] == 0:
        return
    else:
        
        board[x][y] = 0
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < n and 0 <= yy < n  and board[xx][yy] == 1:
                cnt += 1
                DFS(xx, yy)


if __name__ == "__main__":
    n = int(input())
    board = [[0]*n for _ in range(n)]
    ch = [[0]*n for _ in range(n)]
    mt = [list(map(str, input().split())) for _ in range(n)]
    res = []
    cnt = 0
    for i in range(n):
        for j in range(n):
            board[i][j] = int(mt[i][0][j])
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cnt += 1
                DFS(i, j)
                res.append(cnt)
                cnt = 0
    res.sort()
    print(len(res))
    for i in res:
        print(i)
'''
    
    
