import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 

############## 인접행렬 #############


# 한번 방문한 노드는 방문하지 않게 하는 것 중요


def DFS(v):
    global cnt
    if v == n:
        cnt += 1
        #for x in path:
        #    print(x, end = ' ')
        #print()
    else:
        for i in range(1, n+1):
            if g[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                #path.append(i)
                DFS(i)
                #path.pop()
                ch[i] = 0
            
                
            


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [[0] * (n+1) for _ in range(n+1)]
    ch = [0] * (n+1)
    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1
    cnt = 0
    ch[1] = 1 # 요 부분 없어도 돌아가던데
    ######## 경로도 확인하는 코드 ########
    #path = []
    #path.append(1)
    ######################################
    DFS(1)
    print(cnt)

    

'''
### 100점... 해냈다 나란 녀석...
def DFS(L):
    global cnt
    if L == n:
        cnt += 1
        
    else:
        for i in range(n):
            if mat[L-1][i] == 1 and ch[L] == 0:
                ch[L] = 1
                DFS(i+1)
                ch[L] = 0
                
            


if __name__ == "__main__":
    n, m = map(int, input().split())
    mat = [[0] * n for _ in range(n)]
    cnt = 0
    ch = [0] * (n+1)
    for i in range(m):
        a, b = map(int, input().split())
        mat[a-1][b-1] = 1
    DFS(1)
    print(cnt)
'''
