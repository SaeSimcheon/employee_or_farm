import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 


from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
Q = deque()

dis = [[0]*n for _ in range(m)]

for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            Q.append((i, j))

while Q:
    tmp = Q.popleft()
    for i in range(4):
        xx = tmp[0] + dx[i]
        yy = tmp[1] + dy[i]
        if 0 <= xx < m and 0 <= yy < n and board[xx][yy] == 0:
            board[xx][yy] = 1
            dis[xx][yy] = dis[tmp[0]][tmp[1]] + 1 # 날짜 계산하는 방법 내랑 다름
            Q.append((xx, yy))

flag = 1
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            flag = 0
result = 0
if flag == 1:
    for i in range(m):
        for j in range(n):
            if dis[i][j] > result:
                result = dis[i][j]
    print(result)
else:
    print(-1)

'''
##### time limit 때문에 80점
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
Q = deque()
day = 0


# 처음에 시작할 때 익어있는 토마토를 Q에 추가하고 다 익어있을 경우 0을 출력하고 종료
check = 0
for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            Q.append((i, j))
        elif board[i][j] == 0:
            check += 1
            
if check == 0:
    print(0)
    sys.exit()


# 여기서부터 BFS        
while Q:
    
    for i in range(len(Q)):  # DAY 계산하기 위해 Q사이즈로 돌아가고 DAY +1
        tmp = Q.popleft()
        for k in range(4):
            x = tmp[0] + dx[k]
            y = tmp[1] + dy[k]
            if 0 <= x < m and 0 <= y < n and board[x][y] == 0:
                Q.append((x, y))
                board[x][y] = 1
    day += 1


# 만약 다 돌았는데 덜 익은 토마토가 있을 경우 -1 출력하고 종료
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            print(-1)
            sys.exit()

print(day-1)
            
'''
