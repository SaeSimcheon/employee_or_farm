import sys
#sys.stdin = open('input.txt','r')
'''n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
dy = [[0]*n for _ in range(n)] # 그냥 dy를 채운다면?
dy[0][0] = a[0][0]
for i in range(1,n):
    dy[0][i] = dy[0][i-1]+a[0][i]
    dy[i][0] = dy[i-1][0]+a[i][0]
for i in range(1,n):
    for j in range(1,n):
        dy[i][j] = min(dy[i-1][j],dy[i][j-1])+a[i][j]
print(dy[n-1][n-1])'''

# Bottom-up 첫시도 100
# DP 관점에서,,, 이동하는거마다의 에너지를 기록한다고 생각해서 dy를 다 채우면
# 이동은 오른쪽/아래로 밖에 이동 못하니까, dy 칸마다의 에너지를 기록하면 되겠지
# 그리고 에너지를 더하는건,,, 그 이전 경우에서 최소 에너지를 더하면 되겠고

'''def DFS(x,y):
    if dy[x][y]>0:
        return dy[x][y]
    if x==0 and y==0:
        return a[0][0]
    else:
        if x==0:
            dy[x][y]=DFS(x,y-1)+a[x][y]
        elif y==0:
            dy[x][y]=DFS(x-1,y)+a[x][y]
        else:
            dy[x][y]=min(DFS(x-1,y),DFS(x,y-1))+a[x][y]
        return dy[x][y]

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
dy = [[0]*n for _ in range(n)] # 그냥 dy를 채운다면?
print(DFS(n-1,n-1))'''

# Top-down 첫시도 100
# 처음에 DFS로 들어가기전에, 사이드를 채우고 했는데 답이 안나왔음
# 그래서 DFS안에 사이드를 채우는 식으로 했는데 답이 맞네
# 그리고 마지막 else문에서 return을 밖으로 뺐더니 OK


import sys
sys.stdin = open("input.txt", 'r')
if __name__=="__main__":
    n=int(input())
    arr=[list(map(int, input().split())) for _ in range(n)]
    dy=[[0]*n for _ in range(n)]
    dy[0][0]=arr[0][0]
    for i in range(1, n):
        dy[0][i]=dy[0][i-1]+arr[0][i]
        dy[i][0]=dy[i-1][0]+arr[i][0]
    for i in range(1, n):
        for j in range(1, n):
            dy[i][j]=min(dy[i-1][j], dy[i][j-1])+arr[i][j]
    print(dy[n-1][n-1])


def DFS(x, y):
    if dy[x][y]>0:
        return dy[x][y];
    if x==0 and y==0:
        return arr[0][0]
    else:
        if y==0:
            dy[x][y]=DFS(x-1, y)+arr[x][y]
        elif x==0:
            dy[x][y]=DFS(x, y-1)+arr[x][y]
        else:
            dy[x][y]=min(DFS(x-1, y), DFS(x, y-1))+arr[x][y]
        return dy[x][y]

if __name__=="__main__":
    n=int(input())
    arr=[list(map(int, input().split())) for _ in range(n)]
    dy=[[0]*n for _ in range(n)]
    print(DFS(n-1, n-1))