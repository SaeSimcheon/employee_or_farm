'''
미로탐색(DFS)

이거 포함 x;;
if arr[i[0]][i[1]] == 0 and i not in pre >> 과거에 지나왔던 좌표 x

[[0, 0], [1, 0], [2, 0], [2, 1], [2, 2], [3, 2], [4, 2], [5, 2], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6]]

'''

import sys
#sys.stdin = open("in1.txt","r")

arr = [list(map(int,input().split())) for x in range(7)]
'''
arr = [[0,0,0,0,0,0,0],
       [0,1,1,1,1,1,0],
       [0,0,0,1,0,0,0],
       [1,1,0,1,0,1,1],
       [1,1,0,0,0,0,1],
       [1,1,0,1,1,0,0],
       [1,0,0,0,0,0,0]]
'''
move = [[1,0],[0,1],[-1,0],[0,-1]]


ans = 0
def DFS(arr,pre):
    global ans
    if pre[-1] == [6,6]:
        ans += 1
 #       print(pre)
        return

    else:
        post = [[pre[-1][0]+x[0],pre[-1][1]+x[1]] for x in move]
        post = [x for x in post if -1 not in x and 7 not in x]

        for i in post:
            if arr[i[0]][i[1]] == 0 and i not in pre:
                DFS(arr,pre + [i])

DFS(arr,[[0,0]])
print(ans)
