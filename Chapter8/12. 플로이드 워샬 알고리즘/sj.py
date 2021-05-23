import sys
#sys.stdin = open('input.txt','r')
n, m = map(int,input().split())
dy = [[0]*n for _ in range(n)]
# 1. 입력값 다 받고
for _ in range(m):
    a, b, c = map(int,input().split())
    dy[a-1][b-1] = c
# 2. 최소 비용이니까 임의의 max값으로 없는 경로 채워두기
for i in range(n):
    for j in range(n):
        if i!=j and dy[i][j]==0:
            dy[i][j] = 100
# 3. 경로마다 최소비용으로 대체
for k in range(n):
    for i in range(n):
        for j in range(n):
            dy[i][j] = min(dy[i][j], dy[i][k]+dy[k][j])
# 4. 기존 max값으로 표기된거는 없는 경로니 M으로 대체 및 출력
for i in range(n):
    for j in range(n):
        if dy[i][j] == 100:
            dy[i][j] = "M"
        print(dy[i][j], end= ' ')
    print()

# 첫시도 100
# 강의 안보고 푸는데 성공? 뭐지

'''
플로이드-워셜 알고리즘
그래프에서 모든 node->node 경로의 최소 비용
냅색 알고리즘과 동일
'''
# 처음에 갈수 있는 경로로 초기화를 시키고
# i->k->j 를 통해 이중 for문으로 경로를 갱신
# i->k->j 면 k만 거치는거냐? X / i->k 경로에서 중간에 다른 노드를 거치는게 최소일수도 있음

import sys
sys.stdin = open("input.txt", 'r')
if __name__=="__main__":
    n, m=map(int, input().split())
    dis=[[5000]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dis[i][i]=0
    for i in range(m):
        a, b, c=map(int, input().split())
        dis[a][b]=c
    # 여기서부터 플로이드-와샬 알고리즘
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dis[i][j]=min(dis[i][j], dis[i][k]+dis[k][j])
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dis[i][j]==5000:
                print("M", end=' ')
            else:
                print(dis[i][j], end=' ')
        print()