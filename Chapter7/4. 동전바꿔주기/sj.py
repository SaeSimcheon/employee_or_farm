import sys
#sys.stdin = open("input.txt", "rt")
'''def DFS(L,s):
    global cnt
    if s>t:
        return
    if L==k:
        if s==t:
            cnt+=1
    else:
        for i in range(a[L][1]+1):
            DFS(L+1, s+a[L][0]*i)
if __name__=="__main__":
    t = int(input())
    k = int(input())
    a = [list(map(int,input().split())) for _ in range(k)]
    cnt = 0
    DFS(0,0)
    print(cnt)'''

# 첫시도 100
# 이지하군

def DFS(L, sum):
    global cnt
    if sum > m:
        return
    if L == k:
        if sum == T:
            cnt += 1
    else:
        for i in range(cn[L]+1):
            DFS(L+1, sum+(cv[L]*i))

T = int(input())
k = int(input())
cv = list()
cn = list()
for i in range(n):
    a, b = map(int, input().split())
    cv.append(a)
    cn.append(b)
cnt = 0
DFS(0, 0)
print(cnt)

