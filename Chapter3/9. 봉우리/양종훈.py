import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# zero padding
a.insert(0, [0]*n) # 맨 윗줄
a.append([0]*n) # 맨 아랫줄
for x in a:
    x.insert(0, 0) # 왼쪽
    x.append(0) # 오른쪽

cnt = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j] > a[i + dx[k]][j + dy[k]] for k in range(4)): # all() : 안에 조건이 모두가 다 참일 때 참이 되는 것
            cnt += 1
print(cnt)
