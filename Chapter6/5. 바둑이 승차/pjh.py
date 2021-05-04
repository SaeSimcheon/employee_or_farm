import sys

#sys.stdin=open('input.txt','rt')


def DFS(v):
    global ans_sums
    global ans
    global weights
    if v == n+1:
        for i in range(n):
            if ch[i] ==1:
                ans.append(weights[i-1])
        ans_sum = sum(ans)
        ans_sums.append(ans_sum)
                
    else :
        ch[v]=1
        DFS(v+1)
        ch[v]=0
        DFS(v+1)
        
if __name__=="__main__":
    ans_sums = []
    ans = []
    weights = []
    c, n = map(int,input().split())
    ch = [0] * (n+1)
    for i in range(n):
        weights.append(int(input()))
    #print(weights)
    DFS(1)
    #print(ans_sums)
    answer = []
    for i in range(len(ans_sums)):
        if ans_sums[i] <= c:
            answer.append(ans_sums[i])
    print(max(answer))
    



'''
def DFS(L,sum):
    global result
    if sum>c:
        return
    if L==n:
        if sum>result:
            result=sum
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)


if __name__=='__main__':
    c, n = map(int,input().split())
    a = [0]*n
    result = -2147000000
    for i in range(n):
        a[i] = int(input())
    DFS(0,0)

'''
