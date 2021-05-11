import sys

#sys.stdin=open('input.txt','rt')

##n트리

input = sys.stdin.readline #입력 양이 많을 때 속도가 빨라지기 위해

# text 읽을 때는 s = input().rstrip()

def DFS(L,sum,time):
    if time > m :
        return
    if L==n:
        point.append(sum)
    else:
        DFS(L+1,sum+q[L][0],time+q[L][1])
        DFS(L+1,sum,time)
            
    


if __name__=="__main__":
    n, m = map(int, input().split())
    q = list()
    for i in range(n):
        q.append(list(map(int,input().split())))
    point = []
    s = 0
    t = 0
    DFS(0,0,0)
    print(max(point))
