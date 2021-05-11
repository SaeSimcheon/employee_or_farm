import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 

###### BFS ########

# 노드의 레벨별로 탐색
# 큐 자료구조 이용

from collections import deque



# (n//2, n//2) 좌표를 상태트리의 출발점으로
# 다음 노드는 4개의 가지 : 상하좌우
# 탐색한 곳은 체크


# 방향탐색 하는 방법(dx, dy in section2)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
sum = 0

Q = deque()

ch[n//2][n//2] = 1
sum += a[n//2][n//2]

Q.append((n//2, n//2))
L = 0

while True:
    if L == n//2:
        break
    size = len(Q) # 해당 level의 node 개수
    for i in range(size):
        tmp = Q.popleft()
        for j in range(4): # 상하좌우 4개
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if ch[x][y] == 0:
                sum += a[x][y]
                ch[x][y] = 1
                Q.append((x, y))
    L += 1

print(sum)
