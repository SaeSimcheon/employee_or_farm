import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 

def DFS(L):
    global res
    if L == n:
        cha = max(money) - min(money)
        if cha < res:
            tmp = set()
            for x in money:
                tmp.add(x)
            if len(tmp) == 3:
                res = cha
    else:
        for i in range(3):
            money[i] += coin[L]
            DFS(L+1)
            money[i] -= coin[L]
    
        

if __name__ == "__main__":
    n = int(input())
    coin = []
    money = [0] * 3
    for _ in range(n):
        coin.append(int(input()))
    res = 2147000000
    DFS(0)
    print(res)

'''    
# 아니 이거 왜 안되는지 찾아주실 분... 계속 1 나옴
def DFS(L, a, b, c):
    global res
    if max(a, b, c) > sum(money)//2:
        return
    if L == n:
        if len(set([a, b, c])) != 3:
            pass
        diff = max(a, b, c) - min(a, b, c)
        if diff < res:
            res = diff
    else:
        DFS(L+1, a + money[L], b, c)
        DFS(L+1, a, b + money[L], c)
        DFS(L+1, a, b, c + money[L])
    
        

if __name__ == "__main__":
    n = int(input())
    #abc = [0, 0, 0]
    money = list()
    for i in range(n):
        a = int(input())
        money.append(a)
    res = 2147000000
    DFS(0, 0, 0, 0)
    print(res)
'''
