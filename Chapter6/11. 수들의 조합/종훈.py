import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 

########### 이진트리 순회 : 깊이 우선 탐색(DFS) ###############

def DFS(L, s, sum):
    global cnt
    if L == k:
        if sum % m == 0:
            cnt += 1
        #return # 이 자리에 return은 있으나 없으나 if문으로 온 이상 else로 가지 않기 때문에 상관이 없음    
    else:
        for i in range(s, n):
            #res[L] = num[i]
            DFS(L+1, i+1, sum + a[i])
    
        
            

if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    #res = [0] * k
    DFS(0, 0, 0)
    print(cnt)


'''
# 쉽구만 ㅋ 100점

def DFS(L, s):
    global cnt
    if L == k:
        if sum(res) % m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            res[L] = num[i]
            DFS(L+1, i+1)
    
        
            

if __name__ == "__main__":
    n, k = map(int, input().split())
    num = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    res = [0] * k
    DFS(0, 0)
    print(cnt)
'''

