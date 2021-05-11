import sys

#sys.stdin=open('input.txt','rt')

##n트리

input = sys.stdin.readline #입력 양이 많을 때 속도가 빨라지기 위해

# text 읽을 때는 s = input().rstrip()

def DFS(L,sum):
    global weights
    if L == n:
        weights.append(abs(sum))
    else:
        DFS(L+1,sum+chu[L+1])
        DFS(L+1,sum-chu[L+1])
        DFS(L+1,sum)
        

if __name__=="__main__":
    n = int(input())
    chu = list(map(int, input().split()))
    chu.insert(0,0)
    weights = []
    DFS(0,0)
    cnt = weights.count(0)
    for _ in range(cnt):
        del weights[weights.index(0)] # 왜 0 안 없어짐? -> 여러개여서
    #print(set(weights))
    print(sum(chu)-len(set(weights)))

'''
def DFS():
    global res
    if L == n:
        if 0<sum<=s:
            res.add(sum)
    else :
        DFS(L+1,sum+G[L])
        DFS(L+1, sum-G[L])
        DFS(L+1, sum)

if __name__=='__main__':
    n = int(input())
    G= list(map(int, input().split()))
    s = sum(G)
    res = set()
    DFS(0,0)



'''
