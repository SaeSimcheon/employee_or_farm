'''
알리바바와 40인의 도둑(Bottom-Up)
0행 0열 margin 계산 후 비교하면서 계산

n = 3
arr = [[3,3,5],
       [2,3,4],
       [6,5,2]]

n = 5
arr = [[3,7,2,1,9],
       [5,8,3,9,2],
       [5,3,1,2,3],
       [5,4,3,2,1],
       [1,7,5,2,4]]
'''

import sys
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
'''
dy = [[0] * n for i in range(n)]
dy[0][0] = arr[0][0]

move = [[-1,0],[0,-1]]


for i in range(1,n):
    dy[0][i] = dy[0][i-1] + arr[0][i]
    dy[i][0] = dy[i-1][0] + arr[i][0]

for i in range(1,n):
    for j in range(1,n):
        post = [[i+pre[0],j+pre[1]] for pre in move]

        if dy[post[0][0]][post[0][1]] < dy[post[1][0]][post[1][1]]:
            dy[i][j] = dy[post[0][0]][post[0][1]] + arr[i][j]
        else:
            dy[i][j] = dy[post[1][0]][post[1][1]] + arr[i][j]

print(dy[-1][-1])
'''

dy = [[0] * n for _ in range(n)]
dy[n-1][n-1] = arr[n-1][n-1]


for i in range(1,n):
    dy[n-i-1][n-1] = dy[n-i][n-1] + arr[n-i-1][n-1]
    dy[n-1][n-i-1] = dy[n-1][n-i] + arr[n-1][n-i-1]

def DFS(r,c):

    if r==c==n-1:
        return dy[r][c]
        
    else:
        if dy[r+1][c] < dy[r][c+1]:
            dy[r][c] = dy[r+1][c] + arr[r][c]
        else :
            dy[r][c] = dy[r][c+1] + arr[r][c]

for i in range(n-2,-1,-1):
    for j in range(n-2,-1,-1):
        DFS(i,j)
print(dy[0][0])



