import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 

###### BFS ########

# 노드의 레벨별로 탐색
# 큐 자료구조 이용


# 못품... 망할
from collections import deque

board = [list(map(int, input().split())) for _ in range(7)]
dis = [[0]*7 for _ in range(7)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

Q = deque()
Q.append((0, 0))
board[0][0] = 1 # 따로 체크하지 않고 지나간 곳을 벽으로 만들어버리면 다시 안감

while Q: # Q가 비면 멈추도록
    tmp = Q.popleft()
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0 <= x <= 6 and 0 <= y <= 6 and board[x][y] == 0:
            board[x][y] = 1 # 벽으로 만들어 버리기
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1
            Q.append((x, y))

if dis[6][6] == 0:
    print(-1)
else:
    print(dis[6][6])

    
    
'''


a = [list(map(int, input().split())) for _ in range(7)]
ch = [[0]*n for _ in range(7)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

Q = deque()
Q.append((0, 0))

while True:
    if Q[0] == (6, 6):
        print(dis[6][6])
    else:
        tmp = Q.popleft()
        size = len(Q)
        for i in range(size):
            for j in range(4):
                x = tmp[0] + dx[j]
                y = tmp[1] + dy[j]
                if x > 0 and y > 0 and ch[x][y] == 0:
                    ch[x][y] = 1
                
    
'''
