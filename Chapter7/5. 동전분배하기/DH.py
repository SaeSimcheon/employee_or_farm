'''
동전 분배하기
'''

import sys
#sys.stdin = open("in1.txt","r")

n = int(input())
arr = [int(input()) for i in range(n)]

'''
n = 7
arr = [8,9,11,12,23,15,17]
'''
ans = 40000000000
def DFS(li,num,F,S,T):
    global ans
    
    if n == num:
        Max = max(F,S,T)
        Min = min(F,S,T)

        if ans > Max-Min and F != S and F!= T and S != T:
            ans = Max-Min            
        return

    else:
        DFS(li,num+1,F+li[num],S,T)
        DFS(li,num+1,F,S+li[num],T)
        DFS(li,num+1,F,S,T+li[num])
DFS(arr,0,0,0,0)
print(ans)


