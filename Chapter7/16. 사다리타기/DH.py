'''
사다리 타기(DFS)
'''

import sys
#sys.stdin = open("in1.txt")
arr = [list(input().split()) for _ in range(10)]


def DFS(arr,pre):

    if pre[-1][0] == 9:
        if arr[pre[-1][0]][pre[-1][1]] == '2':
            print(pre[0][1])      
        return

    else:
        Temp = pre[-1]
        post = [[Temp[0],Temp[1] + 1],[Temp[0],Temp[1] - 1]]
        post = [x for x in post if -1 not in x and 10 not in x] #bound
        post = [x for x in post if x not in pre and arr[x[0]][x[1]] != "0"] #"0" & pre

        if len(post) != 0:
            DFS(arr,pre + post)
        else:
            DFS(arr,pre + [[Temp[0] + 1,Temp[1]]])


for idx,i in enumerate(arr[0]):
    if i == "1":
        DFS(arr,[[0,idx]])
