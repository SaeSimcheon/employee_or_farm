'''
피자 배달 거리(삼성 SW역량평가 기출문제 : DFS활용)
'''

import sys
#sys.stdin = open("in1.txt")

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
#print(arr)
'''
n,m = 4,4
arr = [[0,1,2,0],
       [1,0,2,1],
       [0,2,1,2],
       [2,0,1,2]]
'''
def dis(ls_house,ls_pizza):
    T = [abs(ls_house[0] - x[0]) + abs(ls_house[1] - x[1]) for x in ls_pizza]
    return min(T)


ls_h = []
ls_p = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            ls_p += [[i,j]]
        elif arr[i][j] == 1:
            ls_h += [[i,j]]

ans = 21476000
def DFS(ls,sel_p):
    global ans
    if len(sel_p) == m:
        ans_ = 0

        for i in ls_h:
            ans_ += dis(i,sel_p)
        
        if ans_ < ans:
            ans = ans_
        return
    elif len(ls) == 0:
        return
       
    else:
        DFS(ls[1:],sel_p + [ls[0]])
        DFS(ls[1:],sel_p)


DFS(ls_p,[])
print(ans)
