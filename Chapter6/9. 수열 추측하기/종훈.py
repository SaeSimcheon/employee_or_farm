import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 

########### 이진트리 순회 : 깊이 우선 탐색(DFS) ###############

### 이항계수 규칙 발견해야함
# n = 3 : (1, 2, 1)
# n = 4 : (1, 3, 3, 1)
# n = 5 : (1, 4, 6, 4, 1)

def DFS(L, sum):
    global cnt
    if L == n and sum == f:
        for x in p:
            print(x, end = ' ')
        # 여러가지 경우가 있을 때 사전 순으로 가장 앞에 오는 것이 최초 발견된 것
        sys.exit(0) # 함수 종료가 아니라 프로그램 전체를 종료
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i
                DFS(L+1, sum + p[L]*b[L])
                ch[i] = 0
                
            else:
                pass
            

if __name__ == "__main__":
    n, f = map(int, input().split())
    p = [0] * n
    b = [1]* n # 이항계수의 맨 끝은 항상 1이라서 1로 초기화
    ch = [0] * (n+1)
    
    # 이항계수 구하는 법 : combination이랑 같음
    for i in range(1, n):
        b[i] = b[i-1] * (n-i) / i
        
    DFS(0, 0)

    

'''
# 이 코드 왜 안되나 한시간째 보고 있었는데 중복허용 안돼서 출력이 없었던거임...
def DFS(L):
    global sum
    if L == n:
        if sum == f:
            for i in range(n):
                print(res[i], end = ' ')
                
    else:
        for i in range(1, n+1):
            ch
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                sum += i
                DFS(L+1)
                ch[i] = 0
                sum -= i
                
            else:
                pass
            

if __name__ == "__main__":
    n, f = map(int, input().split())
    ch = [0] * (n+1)
    res = [0] * (n+1)
    sum = 0
    DFS(0)

'''
