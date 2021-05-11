'''
단지 번호 붙이기(DFS, BFS)

연결된 곳을 저장하는 con [list] 만들
'''

import sys
#sys.stdin = open("in1.txt")
n = int(input())

'''
n = 7
arr = [['0','1','1','0','1','0','0'],
       ['0','1','1','0','1','0','1'],
       ['1','1','1','0','1','0','1'],
       ['0','0','0','0','1','1','1'],
       ['0','1','0','0','0','0','0'],
       ['0','1','1','1','1','1','0'],
       ['0','1','1','1','0','0','0'],]

ls = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == "1":
            ls.append([i,j])
'''


ls = []
for i in range(n):
    for idx,j in enumerate(input()):
        if j == "1":
            ls.append([i,idx])

ans = [] 
while len(ls) !=0:
    
    A = [ls[0]]
    con = [ls[0]]
    ls = ls[1:]

    move = [[0,1],[1,0],[0,-1],[-1,0]]
    while len(A) != 0:

        temp = A.pop(0)
        post = [[temp[0] + x[0], temp[1] + x[1]] for x in move]

        for i in post:
            if i in ls:
                Temp = ls.pop(ls.index(i))
                con += [i]
                A += [i]
    ans.append(con)

ans = sorted(ans, key = lambda x :len(x))
print(len(ans))
for i in ans:
    print(len(i))
