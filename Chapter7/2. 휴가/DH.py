'''
휴가
'''
import sys

#sys.stdin = open("in1.txt","r")

n = int(input())

arr = []
for i in range(n):
    d,v = map(int,input().split())
    arr.append([i,d,v])

#print(arr)
'''

n = 7
arr = [[0,4,20],[1,2,10],[2,3,15],[3,3,20],[4,2,30],[5,2,20],[7,1,10]]
'''

ans = -1

def DFS(ls,start,Sum):
    global ans
    if start >= n:
        if ans < Sum:
            ans = Sum

    else:
        if start + ls[start][1] <= n:
            
            DFS(ls,start + 1, Sum)
            DFS(ls,start + ls[start][1], Sum + ls[start][2])
        else:
            DFS(ls,start + 1, Sum)

DFS(arr,0,0)
print(ans)
