import sys
#sys.stdin = open("input.txt", "rt")


########### 이진트리 순회 : 깊이 우선 탐색(DFS) ###############

##### Cut Edge Tech
# tsum : 부분집합 포함여부와 관계없이 현재까지 고려한 바둑이들의 무게 합.
# total - tsum : 현재 진행단계 이후 고려해야 할 바둑이들의 전체 무게
# sum + (total-tsum) < result : 현재까지 고려한 바둑이들의 무게와 남은 바둑이들의 무게 합이 result보다 작으면 고려할 필요가 없는 부분집합이 됨.


def DFS(L, sum, tsum):
    global result

    #####
    if sum + (total-tsum) < result:
        return
    #####

    if sum > c:
        return
    if L == n:
        if sum > result:
            result = sum
        
    else:
        DFS(L+1, sum + a[L], tsum + a[L]) #
        DFS(L+1, sum, tsum + a[L]) #
            



if __name__ == "__main__":
    c, n = map(int, input().split())
    a = [0] * n
    result = -2147000000
    for i in range(n):
        a[i] = int(input())
    total = sum(a) # 
    DFS(0, 0, 0)
    print(result)



'''
# 최대값 뽑는 방법 바꿨는데 이것도 time limit 40점...
def DFS(x, s):
    global res
    if s > c:
        if res < s-w[x-1]:
            res = s-w[x-1]
        return
    if x == n:
        if res < s:
            res = s
        return
    else:
        DFS(x+1, s+w[x])
        DFS(x+1, s)
            



if __name__ == "__main__":
    c, n = map(int, input().split())
    w = []
    for _ in range(n):
        weight = int(input())
        w.append(weight)
    res = 0
    DFS(0,0)
    print(res)
'''


'''
# 답은 맞는데 time limit 으로 40점...
def DFS(x, s):
    if s > c:
        res.append(s-w[x-1])
        return
    if x == n:
        res.append(s)
        return
    else:
        DFS(x+1, s+w[x])
        DFS(x+1, s)
            



if __name__ == "__main__":
    c, n = map(int, input().split())
    w = []
    for _ in range(n):
        weight = int(input())
        w.append(weight)
    res = []
    DFS(0,0)
    print(max(res))
'''