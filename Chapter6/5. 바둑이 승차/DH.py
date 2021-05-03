'''
바둑이 승차(DFS)

현재까지 더한것 + 남은 거 다 더한 것 < 현재 ans : return


def DFS(L,sum,tsum) :
    global result

    if sum +(total - tsum) < result:
        return
    
    if sum > c:
        return
    
    if L == n:
        if sum > result:
            result = sum
    else:
        DFS(L+1,sum + a[L],tsum + a[L])
        DFS(L+1,sum,tsum + a[L])

if __name__ =="__main__":
    c,n = map(int,input().split())
    #print(c,n)
    a = [0] * n
    result = -21470000

    for i in range(n):
        a[i] = int(input())
    total = sum(a)
    DFS(0,0,0)

    print(result)

'''

import sys

#sys.stdin = open("in2.txt","r")
c,n = map(int,input().split())

arr = [int(input()) for x in range(n)]
total = sum(arr)

ans = -1

def DFS(re,ls):
    global ans

    if not ls:
        if re > ans and re <= c:
            ans = re
        return
    elif re + sum(ls) < ans:
        return
    else:
        DFS(re + ls[0],ls[1:])
        DFS(re ,ls[1:])

DFS(0,arr)
print(ans)

