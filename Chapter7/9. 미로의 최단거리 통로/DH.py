'''
미로의 최단거리 통로(BFS 활용)

import sys

#sys.stdin = open("in4.txt","r")

arr = [list(map(int,input().split())) for _ in range(7)]


ans = 214700000

move = [[1,0],[0,1],[-1,0],[0,-1]]
def BFS(ls,pre,num):
    global ans

    if pre[-1] == [6,6]:
        if ans > num:
            ans = num
        return

    else:
        post = [[pre[-1][0]+x[0],pre[-1][1]+x[1]]for x in move]
        post = [x for x in post if -1 not in x and 7 not in x and ls[x[0]][x[1]] == 0 and x not in pre]

        for i in post:
            BFS(ls,pre + [i],num +1)

BFS(arr,[[0,0]],0)
if ans == 214700000:
    print(-1)
else:
    print(ans)

'''
'''
arr = [[0,0,0,0,0,0,0],
       [0,1,1,1,1,1,0],
       [0,0,0,1,0,0,0],
       [1,1,0,1,0,1,1],
       [1,1,0,1,0,0,0],
       [1,0,0,0,1,0,0],
       [1,0,1,0,0,0,0]]
'''

import sys

#sys.stdin = open("in4.txt","r")

arr = [list(map(int,input().split())) for _ in range(7)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

visit = [[(0,0),0]]
dic = {(0,0) : 0}

while visit:
    tmp,cnt = visit.pop(0)
    possible = [(tmp[0] + dx[i],tmp[1] + dy[i]) for i in range(4)
                if 0<= tmp[0] + dx[i] < 7 and 0<= tmp[1] + dy[i] < 7]
    next_ = []
    for x in possible:
        if arr[x[0]][x[1]] == 0:
            if x not in dic or cnt + 1 < dic[x]:
                dic[x] = cnt + 1
                visit += [[x,cnt+1]]

if (6,6) in dic:
    print(dic[(6,6)])
else:
    print(-1)
