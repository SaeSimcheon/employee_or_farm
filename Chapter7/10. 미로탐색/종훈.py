import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 


# 내 답이랑 다른점
# 답은 DFS 뻗기 전에 조건을 달아줬고
# 나는 DFS 다 뻗고 처음에 조건으로 return을 했음
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    global cnt
    if x == 6 and y == 6:
        cnt += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx <= 6 and 0 <= yy <= 6 and board[xx][yy] == 0:
                board[xx][yy] = 1
                DFS(xx, yy)
                board[xx][yy] = 0



if __name__ == "__main__":
    
    board = [list(map(int, input().split())) for _ in range(7)]
    cnt = 0
    board[0][0] = 1
    DFS(0, 0)
    print(cnt)



'''
# 아니 이걸 한번만에 풀어?? ㅁㅊ....
def DFS(x, y):
    global cnt
    if x < 0 or x > 6 or y < 0 or y > 6 or board[x][y] != 0:
        return
    if x == 6 and y == 6:
        cnt += 1
        return
    else:
        board[x][y] = 1
        for i in range(4):
            DFS(x+dx[i], y+dy[i])
        board[x][y] = 0



if __name__ == "__main__":
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    board = [list(map(int, input().split())) for _ in range(7)]
    cnt = 0
    DFS(0, 0)
    print(cnt)
    
'''
    

    
