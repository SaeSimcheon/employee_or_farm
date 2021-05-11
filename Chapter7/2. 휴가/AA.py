import sys

#sys.stdin=open('input.txt','rt')

##n트리

input = sys.stdin.readline #입력 양이 많을 때 속도가 빨라지기 위해

# text 읽을 때는 s = input().rstrip()
'''
def DFS(L,money,time):
    global res
    if time == n+1:
        return
    else:
        income.append(money)
        DFS(L+time,money+q[time][1],time+q[time][0]) # L+time까진 함
        DFS(L+1, money[L+1], time[L+1])
            
    


if __name__=="__main__":
    n = int(input())
    q = list()
    for i in range(n):
        q.append(list(map(int,input().split())))
    income=[]
    money = 0
    res = -2147000000
    DFS(0,0,0)
    print(max(income))
'''

def DFS(L,sum):
    global res
    if L == n+1:
        if sum > res :
            res = sum
    else:
        if L+T[L] <= n+1 :
            DFS(L+T[L], sum+P[L])
        DFS(L+1,sum)

if __name__=="__main__":
    n = int(input())
    T = [0]
    P = [0]
    for i in range(n):
        a, b = map(int, input().split())
        T.append(a)
        P.append(b)
    res = -2147000000
    DFS(1,0)
    print(res)
