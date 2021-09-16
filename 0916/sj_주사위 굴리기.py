import sys
sys.stdin = open("input.txt", "rt")
n, m, x, y, k = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
K = list(map(int, input().split()))
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
dice = [0]*6
for idx in K:
    xx, yy = x+dx[idx-1], y+dy[idx-1]
    if 0<=xx<n and 0<=yy<m:
        if idx == 1:
            dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
        elif idx == 2:
            dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
        elif idx == 3:
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
        else:
            dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
        if a[xx][yy] == 0:
            a[xx][yy] = dice[5]
        else:
            dice[5] = a[xx][yy]
            a[xx][yy] = 0
        x, y = xx, yy
        print(dice[0])