import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 


def DFS(L, sum):
    global res
    if L == n+1:
        if sum > res:
            res = sum
        #return # 여기 왜 return 없어도 되지...?
    else:
        if L+T[L] <= n+1:
            DFS(L + T[L], sum + P[L])
        DFS(L+1, sum)
        

if __name__ == "__main__":
    n = int(input())
    T = list()
    P = list()
    for i in range(n):
        a, b = map(int, input().split())
        T.append(a)
        P.append(b)
    res = -2147000000
    T.insert(0, 0) # index 맞추기 위해서 하나씩 뒤로 미루는 효과
    P.insert(0, 0)
    DFS(1, 0)
    print(res)


'''
# 쉽노 ㅋ
def DFS(L, sum):
    global res
    # 처음에 이부분 빼먹어서 40점 나옴
    # 주어진 날짜보다 넘어가게 상담을 할 수는 없음
    if L > n: 
        return
    if L == n:
        if sum > res:
            res = sum
        return
    else:
        DFS(L+day[L], sum + cost[L])
        DFS(L+1, sum)
    

if __name__ == "__main__":
    n = int(input())
    day = []
    cost = []
    for i in range(n):
        t, p = map(int, input().split())
        day.append(t)
        cost.append(p)
    res = -2147000000
    DFS(0, 0)
    print(res)
'''
    

