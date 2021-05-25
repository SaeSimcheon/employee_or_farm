import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 

################ 동적 계획법 #################

#### 플로이드 와샬 알고리즘
# 냅섹 알고리즘과 동일한 원리

# dis[i][j] : i에서 j로 가는데 최소 비용

# 와 이거 이렇게 간단하게 된다고...?


if __name__ == "__main__":
    n, m = map(int, input().split())
    dis = [[5000] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dis[i][i] = 0

    for i in range(m):
        a, b, c = map(int, input().split())
        dis[a][b] = c

    ################ 이 부분이 플로이드 와샬 알고리즘 ############
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
    ##############################################################
                
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dis[i][j] == 5000:
                print("M", end = ' ')
            else:
                print(dis[i][j], end = ' ')
        print()

    

'''

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [[0] * n for _ in range(n)]

    for i in range(m):
        a, b, c = map(int, input().split())
        arr[a-1][b-1] = c

    dy = [[1000] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                dy[i][j] = 0
            if dy[i][j] != 0:
                dy[j]
                
'''  
