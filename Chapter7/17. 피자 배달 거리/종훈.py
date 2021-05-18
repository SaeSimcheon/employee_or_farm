import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 

'''
# 이 문제에서 조합 짜는 코드 참고... 이거 까먹어서 못 풀었음
def DFS(L, s):
    global res
    if L == m:
        for x in cb:
            print(x, end = ' ')
        print()
    else:
        for i in range(s, len(pz)):
            cb[L] = i
            DFS(L+1, i+1)
'''

def DFS(L, s):
    global res
    if L == m:
        sum = 0
        for j in range(len(hs)): # 각 집에서
            x1 = hs[j][0]
            y1 = hs[j][1]
            dis = 2147000000
            for x in cb: # 최소거리를 가지는 피자 가게 1개 구하기
                x2 = pz[x][0]
                y2 = pz[x][1]
                dis = min(dis, abs(x1-x2) + abs(y1-y2))
            sum += dis # 모든 집에서 피자 가게까지의 거리 총합
        if sum < res:
            res = sum
                
    else:
        for i in range(s, len(pz)):
            cb[L] = i
            DFS(L+1, i+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    hs = []
    pz = []
    cb = [0] * m # 조합의 경우의 수를 저장하는 리스트
    res = 2147000000
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                hs.append((i, j))
            elif board[i][j] == 2:
                pz.append((i, j))
    DFS(0, 0)
    print(res)
    

'''
# 못품... 조합 코드 까먹은 듯...
def DFS(L, sum):
    global res
    if L == m:
        if sum < res:
            res = sum
    else:
        for i in range(len(pizza)):
            if ch[i] == 0:
                ch[i] = 1
                dis = 0
                for j in range(len(home)):
                    h = abs(pizza[i][0] - home[j][0]) + abs(pizza[i][1] - home[j][1])
                    if h < dis:
                        dis = h
                DFS(L+1, sum + dis)
                ch[i] = 0
        

if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    pizza = []
    home = []
    res = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                pizza.append((i, j))
            elif board[i][j] == 1:
                home.append((i, j))
    ch = [0]*len(pizza)
    DFS(0, 0)
    print(res)
'''
