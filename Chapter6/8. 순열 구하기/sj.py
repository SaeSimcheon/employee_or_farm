import sys
#sys.stdin = open("input.txt", "rt")
'''def DFS(L):
    global cnt
    if L==m:
        if len(res[:m]) == len(set(res[:m])):
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
'''
# 첫시도 100
# 중복순열과 같게 코드를 짰지만, 순열이 중복되지 않는거만 print

def DFS(L):
    global cnt
    if L==m:
        for j in range(L):
            print(res[j], end = ' ')
        print()
        cnt += 1
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                DFS(L+1)
                ch[i]=0 # 앞 코드를 취소시키는 용도

if __name__=="__main__":
    n, m = map(int,input().split())
    res=[0]*n
    ch = [0]*(n+1)
    cnt = 0
    DFS(0)
    print(cnt)

# 배운점
# 1. 순열의 경우 checklist를 따로 만들어서, 숫자가 다시 나오지 않도록 cutoff를 만들어주어야함
# checklist를 다시 초기화시키는것도 중요,
# DFS 뒤에 코드를 넣으면 다시 돌아와서 실행된다는걸 기억하자