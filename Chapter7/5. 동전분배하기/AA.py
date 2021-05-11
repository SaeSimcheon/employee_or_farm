import sys
#sys.stdin=open('input.txt','rt')

##n트리

input = sys.stdin.readline #입력 양이 많을 때 속도가 빨라지기 위해

# text 읽을 때는 s = input().rstrip()

def DFS(L,sum1,sum2,sum3):
    global n,a,res
    if L == n:
        diff = min([abs(sum1-sum2),abs(sum2-sum3),abs(sum3-sum1)])
        if diff < res :
            res = diff
    else:
        DFS(L+1,sum1+a[L+1],sum2,sum3)
        DFS(L+1,sum1,sum2+a[L+1],sum3)
        DFS(L+1,sum1,sum2,sum3+a[L+1])

if __name__=="__main__":
    n = int(input())
    a = list()
    for _ in range(n):
        a.append(int(input()))
    a.insert(0,0)
    res = 2147000000
    DFS(0,0,0,0)
    print(res)
