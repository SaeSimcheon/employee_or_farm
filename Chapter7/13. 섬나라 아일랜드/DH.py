'''
섬나라 아일랜드(BFS 활용)
'''

import sys
#sys.stdin = open("in1.txt")

n = int(input())
ls = []

for i in range(n):
    for idx,j in enumerate(input().split()):
        if j == "1":
            ls.append([i,idx])

'''
n = 7
arr = [[1,1,0,0,0,1,0],
       [0,1,1,0,1,1,0],
       [0,1,0,0,0,0,0],
       [0,0,0,1,0,1,1],
       [1,1,0,1,1,0,0],
       [1,0,0,0,1,0,0],
       [1,0,1,0,1,0,0]]

ls = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            ls.append([i,j])
'''
move = [[1,0],[0,1],[1,1],
        [-1,0],[0,-1],[-1,-1],
        [1,-1],[-1,1]]

ans = []
while len(ls) != 0:
    A = [ls[0]]
    con = [ls[0]]
    ls = ls[1:]


    while len(A) != 0:
        temp = A.pop(0)
        post = [[temp[0] + x[0],temp[1] + x[1]] for x in move]

        for i in post:
            if i in ls:
                Temp = ls.pop(ls.index(i))
                con += [Temp]
                A += [Temp]
    ans.append(con)

print(len(ans))

