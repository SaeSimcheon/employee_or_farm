import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 


# 와 답이랑 비슷한데 난 한번에 바로 cut 적용시켰네... 미쳐버렸군

def DFS(L, sum):
    global cnt
    if sum > T:
        return
    if L == k:
        if sum == T:
            cnt += 1
    else:
        for i in range(cn[L]+1):
            DFS(L+1, sum + (cv[L] * i))
        

if __name__ == "__main__":
    T = int(input())
    k = int(input())
    cv = list()
    cn = list()
    cnt = 0

    for i in range(k):
        a, b = map(int, input().split())
        cv.append(a)
        cn.append(b)

    DFS(0, 0)
    print(cnt)


'''
# 오 시간 오래걸리는데 100점 나옴
def DFS(L, sum):
    global cnt
    
    if sum == T:
        cnt += 1
        return # 여기 return 안해서 처음에 틀림
    if sum > T or L == K:
        return

    else:
        for i in range(n[L]+1):
            DFS(L+1, sum+p[L]*i)
        

if __name__ == "__main__":
    T = int(input())
    K = int(input())
    p = list()
    n = list()
    cnt = 0

    for i in range(K):
        a, b = map(int, input().split())
        p.append(a)
        n.append(b)

    DFS(0, 0)
    print(cnt)
    
'''
