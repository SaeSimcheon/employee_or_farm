import sys
sys.stdin = open("input.txt", "rt")
'''def DFS(v):
    global cnt
    if v==m:
        for i in range(m):
            print(check[i], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            check[v]=i
            DFS(v+1)
if __name__=="__main__":
    n, m = map(int,input().split())
    check=[0]*n
    cnt = 0
    DFS(0)
    print(cnt)'''

# 가지가 여러개인 상태트리 / 한 레벨에서 n개만큼 가지가 뻗는 구조

input = sys.stdin.readline # 문자열이 여러개 있을때 입력속도가 빠름
#s = input().rstrip()

def DFS(L):
    global cnt
    if L==m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            res[L]=i
            DFS(L+1)

if __name__=="__main__":
    n, m = map(int,input().split())
    res=[0]*n
    cnt = 0
    DFS(0)
    print(cnt)

# 배운점
# 1. 가지가 여러개인 상태트리 형태 문제, m만큼 가지 갯수를 생성
# 2. 상태트리에서 stack 구조와 트리 구조를 잘 생각하기