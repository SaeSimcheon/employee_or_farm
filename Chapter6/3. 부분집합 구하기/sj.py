import sys
#sys.stdin=open("input.txt", "rt")
'''def DFS(x):
    if x>n:
        return
    else:
        for i in range(x,n+1):
            print(i, end=' ')
        print()
        DFS(x*2)
        DFS(x*2+1)

if __name__=="__main__":
    n = int(input())
    DFS(1)'''

# 모르겠다

# 1,2,3들이 각각 들어가는지 안들어가는지로 부분집합 정의
# 상태트리
# DFS(1) -> O D(2) -> O D(3)
#                  -> X D(3)
#        -> X D(2) -> O D(3)... 이런식으로 D(4)가 되면 if문 종료

def DFS(v):
    if v==n+1:# D(4)일땐 종료지점
        for i in range(1,n+1):
            if check[i]==1:
                print(i, end=' ')
        print()
    else:
        check[v] = 1 # O check
        DFS(v+1) # 다음 노드로 호출
        check[v] = 0 # X check
        DFS(v+1) # 다음 노드로 호출

if __name__=="__main__":
    n = int(input())
    check=[0]*(n+1) # 원소가 들어가는지 안들어가는지 check용도
    DFS(1)

# 배운 점
# 1. 상태트리 구조 -> DFS 문제는 상태트리를 잘 짜는것
# 백트래킹: 모든 경우의 수를 고려하는 알고리즘으로,
# 모든 가능한 케이스가 나열된 상태공간트리를 작성해서 문제를 푼다.
# 백트래킹의 종류로 DFS/BFS가 있으며
# 모든 경우의 수를 구해야 할 때는 DFS,
# 최단거리를 구할 때는 BFS를 사용해서 문제를 푼다.