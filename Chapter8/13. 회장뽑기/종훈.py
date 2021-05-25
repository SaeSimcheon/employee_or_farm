import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 

################ 동적 계획법 #################

#### 플로이드 와샬 알고리즘
# 냅섹 알고리즘과 동일한 원리

if __name__ == "__main__":
    n = int(input())
    dis = [[100] * (n+1) for _ in range(n+1)]
    dy = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dis[i][i] = 0

    while True:
        a, b = map(int, input().split())
        if a == -1 and b == -1:
            break
        else:
            dis[a][b] = 1
            dis[b][a] = 1

    ################ 이 부분이 플로이드 와샬 알고리즘 ############
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
                
    ##############################################################

    res = [0] * (n+1)
    score = 100 # 최소값 저장하기 위해
    for i in range(1, n+1):
        for j in range(1, n+1):
            res[i] = max(res[i], dis[i][j])
        score = min(score, res[i])

    out = []
    for i in range(1, n+1):
        if res[i] == score:
            out.append(i)

    print("%d %d" %(score, len(out)))
    for x in out:
        print(x, end = ' ')
        



'''
# 몰라 ㅡㅡ

if __name__ == "__main__":
    n = int(input())
    dis = [[0] * (n+1) for _ in range(n+1)]
    dy = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dis[i][i] = 0

    for i in range(2147000000):
        a, b = map(int, input().split())
        if a == -1 and b == -1:
            break
        else:
            dis[a][b] = 1
            dis[b][a] = 1

    ################ 이 부분이 플로이드 와샬 알고리즘 ############
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dis[i][j] == 0:
                    dis[i][k] + dis[k][j]
                else:
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
                
    ##############################################################
                
    print(dis)    

    

'''

