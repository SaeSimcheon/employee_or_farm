import sys
#sys.stdin=open("input.txt", "rt")
'''def DFS(v):
    if v==n+1:# D(4)일땐 종료지점
        subset1 = []
        subset2 = []
        for i in range(n):
            if check[i]==1:
                subset1.append(a[i])
            else:
                subset2.append(a[i])
        else:
            if sum(subset1)==sum(subset2):
                print("YES")
                sys.exit(0)
    else:
        check[v] = 1 # O check
        DFS(v+1) # 다음 노드로 호출
        check[v] = 0 # X check
        DFS(v+1) # 다음 노드로 호출
    return cnt
if __name__=="__main__":
    n = int(input())
    a = list(map(int,input().split()))
    check=[0]*(n+1)
    DFS(1)
    print("NO")'''

# 첫시도 100
# 재귀 내에서 subset끼리의 합을 비교
# 같으면 YES 출력하고 종료를 해야하는데, break는 안되고 이것저것 해보다
# 아예 모르겠어서 sys.exit() 검색해서 풀었음
def DFS(L,sum):
    if sum>total//2: # sum이 기준을 넘으면 더 할 필요없으니 return
        return
    if L==n:
        if sum==(total-sum):
            print("YES")
            sys.exit(0) # 프로그램 종료시키기(함수 종료가 아니라)
    else:
        DFS(L+1, sum+a[L]) # 왼쪽
        DFS(L+1, sum) # 오른쪽
if __name__=="__main__":
    n = int(input())
    a = list(map(int,input().split()))
    total = sum(a)
    DFS(0,0)
    print("NO") # 재귀가 다 돌고 아무런 결과가 없으면 NO 출력

# 느낀점
# 1. 부분집합을 하나 만들면 나머지가 다른 부분집합이 된다는 점은 같음
# 2. 답안 코드가 좀더 효율적인거 같다

# 배운점
# 1. DFS(L+1,sum+a[L])처럼 더해주면서 진행가능
# 2. sys.exit(0) -> 더 할 필요없을때 종료
