import sys

#sys.stdin=open('input.txt','rt')

##n트리

input = sys.stdin.readline #입력 양이 많을 때 속도가 빨라지기 위해

# text 읽을 때는 s = input().rstrip()

def DFS(L):
    global cnt
    if L==m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            res[L]=i
            DFS(L+1)



if __name__=="__main__":
    n, m = map(int, input().split())
    res = [0]*m
    cnt=0
    DFS(0)
    print(cnt)
