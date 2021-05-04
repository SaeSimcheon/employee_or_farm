import sys
#sys.stdin = open("input.txt", "rt")
'''def DFS(S,L):
    global cnt
    if S==m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt+=1
    else:
        for p in range(L,n+1):
            res[S]=p
            DFS(S+1,L+p)
if __name__=="__main__":
    n, m = map(int,input().split())
    res=[0]*n
    cnt = 0
    DFS(0,1)
    print(cnt)'''
# 첫시도 100
# 하긴했는데 왜 되는건지는 정확히 모르겠음 -> 강의를 보자

# 이 문제는 굉장히 중요 / 응용의 첫단계 / 상태트리가 약간 다름

def DFS(L,s): #s부터 가지가 뻗는 형태
    global cnt
    if L==m:
        for j in range(m):
            print(res[j], end = ' ')
        print()
        cnt+=1
    else:
        for i in range(s, n+1):
            res[L]=i
            DFS(L+1, i+1) # level은 1 증가, 2번째 가지는 다음 레벨에 2번쨰 가지부터~


if __name__=="__main__":
    n, m = map(int,input().split())
    res=[0]*(n+1)
    cnt = 0
    DFS(0,1)
    print(cnt)

# 배운점
# 1. 상태트리가 다른 형태 / 가지가 제한되게 뻗는 경우
# 순열은 반복문을 항상 처음 숫자부터 시작해도 되지만, 조합은 다음 레벨에서는 +1부터 시작한다.
