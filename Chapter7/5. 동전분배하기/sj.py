import sys
#sys.stdin = open("input.txt", "rt")
'''def DFS(L,a,b,c):
    global minimum
    if L==n:
        if a == b or b == c or a == c:
            return
        else:
            #print(a,b,c)
            diff = max(a,b,c)-min(a,b,c)
            if minimum > diff:
                minimum = diff

    else:
        DFS(L+1,a+coin[L],b,c)
        DFS(L+1,a,b+coin[L],c)
        DFS(L+1,a,b,c+coin[L])

if __name__=="__main__":
    n = int(input())
    coin = [int(input()) for _ in range(n)]
    minimum = 2147000000
    DFS(0,0,0,0)
    print(minimum)'''

# 첫시도 100
# 이지하네

def DFS(L):
    global res
    if L==n:
        cha=max(money)-min(money)
        if cha<res:
            tmp=set()
            for x in money:
                tmp.add(x)
            if len(tmp)==3:
                res=cha
    else:
        for i in range(3):
            money[i]+=coin[L]
            DFS(L+1)
            money[i]-=coin[L]

if __name__=="__main__":
    n=int(input())
    coin=[]
    tmp=[]
    money=[0]*3
    res=2147000000
    for _ in range(n):
        coin.append(int(input()))
    DFS(0)
    print(res)

# 배운점
# 1. set 자료구조를 이용하면 서로 같은 경우를 제거하고 할 수 있음