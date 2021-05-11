'''
등산경로(DFS)
문제 설명

그 구역의 위, 아래, 왼쪽, 오른쪽 중 더 높은
구역으로만 이동할 수 있도록 등산로를 설계하려고 합니다
>>
현재 지점보다 높으면 갈 수 있는 듯

'''

import sys
#sys.stdin = open("in1.txt","r")

n = int(input())

arr = []

Max = -1
Min = 2144990000

s = []
e = []

for i in range(n):
    ls = list(map(int,input().split()))
    arr.append(ls)

    mi = min(ls)
    ma = max(ls)

    if mi < Min:
        s = [i,ls.index(mi)]
        Min = mi
    if ma > Max:
        e = [i,ls.index(ma)]
        Max = ma
'''

n = 5
arr = [[2,23,92,78,93],
       [59,50,48,90,80],
       [30,53,70,75,96],
       [94,91,82,89,93],
       [97,98,95,96,100]]

s = [0,0]
e = [4,4]
'''
ans = 0

move = [[0,1],[1,0],[-1,0],[0,-1]]

def DFS(ls,s):
    global ans
    if s == e:
        ans += 1
        return

    else :
        post = [[s[0] + x[0],s[1] + x[1]] for x in move]
        post = [x for x in post if -1 not in x and n not in x]
        for i in post:
            if ls[s[0]][s[1]] < ls[i[0]][i[1]]:
                DFS(ls,i)
DFS(arr,s)
print(ans)
