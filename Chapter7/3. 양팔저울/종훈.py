import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 


def DFS(L, sum):
    global res
    if L == n:
        if 0 < sum <= s:
            res.add(sum)

    else:
        DFS(L+1, sum + G[L])
        DFS(L+1, sum - G[L])
        DFS(L+1, sum)
        

if __name__ == "__main__":
    n = int(input())
    G = list(map(int, input().split()))
    s = sum(G)
    res = set()
    DFS(0, 0)
    print(s - len(res))



'''
# 쉽구만 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
def DFS(L, sum):
    if L == k:
        a.append(abs(sum))
        return
    else:
        DFS(L+1, sum + w[L])
        DFS(L+1, sum - w[L])
        DFS(L+1, sum)
    
        

if __name__ == "__main__":
    k = int(input())
    w = list(map(int, input().split()))
    #all = list(range(1, sum(w)+1))
    a = list()
    DFS(0, 0)
    l1 = len(list(set(a)))
    print(sum(w)-l1+1) # 0이 포함되어 있어서 +1 해줌
'''
    
