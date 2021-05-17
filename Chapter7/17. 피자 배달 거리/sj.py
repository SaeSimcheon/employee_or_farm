import sys
#sys.stdin = open("input.txt", "rt")
def DFS(S,L):
    global maximum
    if S==m:
        dis = 0
        for i in range(len(house)):
            hx = house[i][0]
            hy = house[i][1]
            dis1 = 2147000000
            for j in res:
                px = pizza[j][0]
                py = pizza[j][1]
                dis1 = min(dis1, abs(hx-px)+abs(hy-py))
            dis += dis1
        if dis<maximum:
            maximum=dis
    else:
        for p in range(L,len(pizza)):
            res[S]=p
            DFS(S+1,p+1)

if __name__=="__main__":
    n, m = map(int,input().split())
    B = [list(map(int, input().split())) for _ in range(n)]
    pizza = [(i,j) for i in range(n) for j in range(n) if B[i][j]==2]
    house = [(i,j) for i in range(n) for j in range(n) if B[i][j]==1]
    maximum = 2147000000
    res = [0]*m
    DFS(0,0)
    print(maximum)

# 피자집을 4개 선택(조합) / L=m(4)일때 stop
# if문에서 거리 계산해서 최소인거를 합산 print

# 근데 어떻게 전개해야할지 모르겠어서 강의보고 해결

def DFS(L, s):
    global res
    if L == m:
        sum = 0
        for j in range(len(hs)):
            x1 = hs[j][0]
            y1 = hs[j][1]
            dis = 2147000000
            for x in cb:
                x2 = pz[x][0]
                y2 = pz[x][1]
                dis = min(dis, abs(x1 - x2) + abs(y1 - y2))
            sum += dis
        if sum < res:
            res = sum
    else:
        for i in range(s, len(pz)):
            cb[L] = i
            DFS(L + 1, i + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    hs = []
    pz = []
    cb = [0] * m
    res = 2147000000
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                hs.append((i, j))
            elif board[i][j] == 2:
                pz.append((i, j))
    DFS(0, 0)
    print(res)

