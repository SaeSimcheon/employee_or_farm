import sys

#sys.stdin=open('input.txt','rt')

##n트리

input = sys.stdin.readline #입력 양이 많을 때 속도가 빨라지기 위해

# text 읽을 때는 s = input().rstrip()

def DFS(L, s):
    global change
    global cnt
    if s > change :
        cnt = L
        return 
    else:
        for i in range(0,n):
            s += coin[i]
            DFS(L+1, s)



if __name__=="__main__":
    s = 0
    cnt = 0
    n = int(input())
    coin = list(map(int,input().split()))
    m = int(input())
    change = m - max(coin)*(m//max(coin))
    if change == 0:
        print(m//max(coin))
    else:
        DFS(0, 0)
    print(cnt + m//max(coin))

'''

def DFS(L,sum):
    if sum > change:
        return
    if sum == change:
        cnt = L
    else:
        for i in range(n):
            DFS(L+1, sum+coin[i])

if __name__=='__main__':
    n - int(input())
    a = list(map(int,input().split()))
    m = int(input())
    res = 2147000000
    DFS(0,0)

'''




