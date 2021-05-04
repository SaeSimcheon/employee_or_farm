import sys
#sys.stdin = open("input.txt", "rt")


########### 이진트리 순회 : 깊이 우선 탐색(DFS) ###############

def DFS(L, sum): # L : 트리의 LEVEL이자 a의 인덱스, sum : 내가 만드는 부분집합의 합
    if sum > total//2: # total의 1/2보다 sum이 커져버리면 당연히 안되는 경우기 때문에 시간복잡도 줄임.
        return
    if L == n:
        if sum == (total - sum):
            print("YES")
            sys.exit(0) # sys.exit(0) : 함수가 종료되는 것이 아니라 프로그램을 종료
    else:
        DFS(L+1, sum + a[L]) 
        DFS(L+1, sum)

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
    print("NO") # 프로그램이 종료된 것이 아니라 계속 톨아갔을 때 NO를 출력



'''
# 실패

def DFS(v):
    if v == n:
        res1 = []
        res2 = []
        for i in range(n):
            if ch[i] == 1:
                res1.append(a[i])
            else:
                res2.append(a[i])
        s1 = sum(res1)
        s2 = sum(res2)
        if s1 == s2:
            b += 1
        return
    else:
        ch[v] = 1
        DFS(a[v+1])
        ch[v] = 0
        DFS(a[v+1])



if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    a.append(0)
    
    ch = [0] * n
    b = 0
    DFS(0)
    if b != 0:
        print("YES")
    else:
        print("NO")
'''

'''
# 모든 부분집합 조합들의 합을 구해서 합이 같은 게 있으면 YES라고 생각했는데 다시 생각해보니 안되는 알고리즘..
# 80점도 과하다
def DFS(v):
    if v == n:
        res = []
        for i in range(n):
            if ch[i] == 1:
                res.append(a[i])
        s = sum(res)
        b[s] = b.get(s, 0) + 1

        
        return
    else:
        ch[v] = 1
        DFS(a[v+1])
        ch[v] = 0
        DFS(a[v+1])



if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    ch = [0] * n
    b = dict()
    DFS(1)
    print(b)
    for key, val in b.items():
        if val > 2:
            print("YES")
            break
    else:
        print("NO")
'''