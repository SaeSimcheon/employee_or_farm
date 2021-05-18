import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 


def DFS(x, y):
    ch[x][y] = 1 # 체크리스트 체크
    if x == 0:
        print(y)
        #break # 여기 이거 넣으면 왜 break outside loop 나오지...?
    else:
        if y-1 >= 0 and board[x][y-1] == 1 and ch[x][y-1] == 0:
            DFS(x, y-1)
        elif y+1 < 10 and board[x][y+1] == 1 and ch[x][y+1] == 0:
            DFS(x, y+1)
        else:
            DFS(x-1, y)

if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(10)]
    ch = [[0]*10 for _ in range(10)] # 나랑 다르게 체크리스트 체크하면서 가서 굳이 시작점 옮겨 줄 필요 없어짐.
    for y in range(10):
        if board[9][y] == 2:
            DFS(9, y)



'''
# 이것도 계속 40점 60점 왔다리 갔다리

dx = [-1, 0, 0, 0, 0]
dy = [0, 1, -1, 3, -3]

def DFS(x, y):
    if x == 0:
        print(y)
        sys.exit()
    else:
        for i in range(1, 3):
            xx = x + dx[i]
            yy1 = y + dy[i]
            yy2 = y + dy[i+2] # 옆옆칸에 아니라 세칸 떨어져 있는 라인이 있어서 고려해 줌.
            if 0 <= xx < 10 and 0 <= yy1 < 10 and 0 <= yy2 < 10 and board[xx][yy1] == 1 and board[xx][yy2] == 0:
                DFS(xx + dx[0], yy1 + dy[i]) # 다음 지점을 옮겨줌
            elif 0 <= xx < 10 and 0 <= yy1 < 10 and 0 <= yy2 < 10 and board[xx][yy1] == 1 and board[xx][yy2] == 1:
                DFS(xx + dx[0], yy2)
            elif 0 <= xx < 10 and 0 <= yy1 < 10:
                DFS(x + dx[0], y + dy[0])


if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(10)]
    for i in range(10):
        if board[9][i] == 2:
            DFS(9, i)
    
'''






'''
#### BFS 인줄 알고 계속 이걸로 풀었네
# 근데 왜 자꾸 수정할 때마다 다른 문제로 틀리고 40점 60점 왔다리갔다리함?
from collections import deque


dx = [-1, 0, 0, 0, 0]
dy = [0, 1, -1, 3, -3]

board = [list(map(int, input().split())) for _ in range(10)]
Q = deque()

#print(board)

for i in range(10):
    if board[9][i] == 2:
        Q.append((9, i))

while True:
    tmp = Q.popleft()
    if tmp[0] == 0:
        print(tmp[1])
        break
    else:
        for i in range(1, 3):
            xx = tmp[0] + dx[i]
            yy1 = tmp[1] + dy[i]
            yy2 = tmp[1] + dy[i+2]
            if 0 <= xx < 10 and 0 <= yy1 < 10 and 0 <= yy2 < 10 and board[xx][yy1] == 1 and board[xx][yy2] == 0:
                Q.append((xx-1, yy1 + dy[i]))
                break
            elif 0 <= xx < 10 and 0 <= yy1 < 10 and 0 <= yy2 < 10 and board[xx][yy1] == 1 and board[xx][yy2] == 1:
                Q.append((xx-1, yy2))
                break
        else:
            xx = tmp[0] + dx[0]
            yy = tmp[1] + dy[0]
            Q.append((xx, yy))
'''
