import sys
#sys.stdin = open("input.txt", "rt")
'''def fac(k):
    ans = 1
    for j in range(2, k+1):
        ans *= j
    return ans
def bcoef(k, r):
    return fac(k)//fac(r)//fac(k-r)
def DFS(L, sum):
    if L==n and sum==f:
        for j in num:
            print(j, end=' ')
        sys.exit(0)
    else:
        for p in range(1,n+1):
            if ch[p]==0:
                ch[p]=1
                num[L]=p
                DFS(L+1, sum+num[L]*coef[L])
                ch[p]=0

if __name__=="__main__":
    n, f = map(int,input().split())
    num = [0]*n
    coef = [1]*n
    ch = [0]*(n+1)
    for i in range(1,n-1):
        coef[i] = bcoef(n-1,i)
    DFS(0,0)'''
# 첫시도 100
# n개의 순열을 만들고 더하는 과정을 반복하는 형태
# a,b,c,d,... 등 n개의 수를 생각하면 f는 a+()b+()c+...
# 여기서 계수가 이항계수니까 이항계수를 따로 함수로 만들었음

def DFS(L, sum):
    if L==n and sum==f:
        for x in p:
            print(x, end = ' ')
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1
                p[L]=i
                DFS(L+1, sum+(p[L]*b[L]))
                ch[i]=0

if __name__=="__main__":
    n, f = map(int,input().split())
    p = [0]*n
    b = [1]*n
    ch = [0]*(n+1)
    for i in range(1,n):
        b[i] = b[i-1]*(n-i)/i # 이항계수를 직접 식으로 구현
    DFS(0, 0)

# 배운점
# 1. 비슷하게 접근 / 이항계수를 함수를 안만들고도 할수 있다.. .아직 부족한듯

# itertools를 이용한 수열 추측하기
import sys
import itertools as it
sys.stdin = open("input.txt", "rt")
n, f = map(int, input().split())
b = [1]*n
for i in range(1, n):
    b[i] = b[i-1]*(n-i)/i
a = list(range(1, n+1))
'''for tmp in it.permutations(a,3): # 순열 출력하는 itertools 함수
    print(tmp)
    cnt+=1
print(cnt)'''
for tmp in it.permutations(a):
    sum=0
    for L, x in enumerate(tmp):
        sum+=(x*b[L])
    if sum==f:
        for x in tmp:
            print(x, end=' ')
        break # 답이 나오면 맨앞의 for문을 멈추는 용도
