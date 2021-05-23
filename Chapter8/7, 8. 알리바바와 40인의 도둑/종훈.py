import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 

################ 동적 계획법 #################

### Top-Down : 역으로 DFS

def DFS(x, y):
    if dy[x][y] > 0: # 메모이제이션 cut-edge
        return dy[x][y]
    if x == 0 and y == 0:
        return arr[0][0]
    else:
        if y == 0:
            dy[x][y] = DFS(x-1, y) + arr[x][y] # 메모이제이션
            # return DFS(x-1, y) + arr[x][y] # 메모이제이션 안 할 경우
        elif x == 0:
            dy[x][y] = DFS(x, y-1) + arr[x][y]
            # return DFS(x, y-1) + arr[x][y]
        else:
            dy[x][y] = min(DFS(x-1, y), DFS(x, y-1)) + arr[x][y]
            # return min(DFS(x-1, y), DFS(x, y-1)) + arr[x][y]
        return dy[x][y]
        


if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0]*n for _ in range(n)] # 메모이제이션을 위해

    print(DFS(n-1, n-1))
    


'''
### Bottom-Up

if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0]*n for _ in range(n)]

    dy[0][0] = arr[0][0]

    # 답은 가장자리 따로 입력하고 for문 돌림
    for i in range(n):
        dy[0][i] = dy[0][i-1] + arr[0][i]
        dy[i][0] = dy[i-1][0] + arr[i][0]

    for i in range(1, n):
        for j in range(1, n):
            dy[i][j] = min(dy[i-1][j], dy[i][j-1]) + arr[i][j]
    print(dy[n-1][n-1])
'''

'''
## 100점. 완벽.
if __name__ == "__main__":
    n = int(input())
    stone = [list(map(int, input().split())) for _ in range(n)]
    
    dy = [[0]*n for _ in range(n)]
    #print(dy)
    dy[0][0] = stone[0][0]
    
    for i in range(n):
        for j in range(n):
            if i == 0 and j > 0: # x축 젤 위에 라인 따로
                dy[i][j] = dy[i][j-1] + stone[i][j]
            elif j == 0 and i > 0: # y축 젤 왼쪽 라인 따로
                dy[i][j] = dy[i-1][j] + stone[i][j]
            elif i != 0 and j != 0: # (0,0) 제외 나머지 따로
                dy[i][j] = min(dy[i-1][j], dy[i][j-1]) + stone[i][j]
    print(dy[n-1][n-1])
'''

