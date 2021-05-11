import sys
#sys.stdin = open("input.txt", "rt")
'''def DFS(L,sum):
    if L==k:
        if 1<=sum and sum<=s:
            res.append(sum)
    else:
        DFS(L+1,sum+a[L])
        DFS(L+1,sum-a[L])
        DFS(L+1,sum)


if __name__=="__main__":
    k = int(input())
    a = list(map(int,input().split()))
    s = sum(a)
    res = []
    DFS(0,0)
    print(s-len(set(res)))
'''
#첫시도 100
# 사칙연산 case(+ or -) 로 1~s 까지의 숫자를 만드는 과정
# 과정을 마치고 나면 중복 제거해서 갯수 찾기

def DFS(L, sum):
    global res
    if L == n:
        if 0 < sum <= s:
            res.add(sum)
    else:
        DFS(L + 1, sum + G[L])
        DFS(L + 1, sum - G[L])
        DFS(L + 1, sum)

if __name__ == "__main__":
    n = int(input())
    G = list(map(int, input().split()))
    s = sum(G)
    res = set()
    DFS(0, 0)
    print(s - len(res))

# 배운점
# 1. set 자료구조에는 set.add()로 추가
# 2. condition에 a<b<c 가 가능하네(R에선 안됨)


