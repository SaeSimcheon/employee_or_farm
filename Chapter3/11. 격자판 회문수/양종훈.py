import sys
#sys.stdin = open("input.txt", "rt")

board = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
for i in range(3):
    for j in range(7):
        tmp = board[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1
        for k in range(2):
            if board[i+k][j] != board[i+5-k-1][j]:
                break
        else:
            cnt += 1

print(cnt)

'''
a = [list(map(int, input().split())) for _ in range(7)]
#print(a[0][0:5][:2])
cnt = 0
for i in range(7):
    for j in range(3):
        if a[i][j:j+5] == a[i][j:j+5][::-1]:
            cnt += 1
        if a[j][i] == a[j+4][i] and a[j+1][i] == a[j+3][i]:
            cnt += 1
print(cnt)
'''