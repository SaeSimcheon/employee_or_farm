import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 

########### 이진트리 순회 : 깊이 우선 탐색(DFS) ###############




### 아 이거 내가 했던거 날라감... 

def DFS(L):
    global cnt
    if L == m:
        for j in range(m):
            print(res[j], end = ' ')
        print()
        cnt += 1
    else:
        for j in range(1, n+1):
            res[L] = i
            DFS(L+1)
            
        

if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0]*m
    cnt = 0
    DFS(0)
    print(cnt)



'''
def DFS(L, money):
    global cnt
    global res
    if res < cnt:
        cnt = 0
        return
    if money == 0:
        res = cnt
        return
    else:
        
        b = m // L
        for j in range(b+1):
            cnt += j
            DFS(L, money-b*j)
            
        

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    res = 0
    #DFS(m)
    a.sort(reverse = True)
    for i in a:
        DFS(i, m)
    print(res)
'''


'''
# 이거 왜 80점..?
# 아 젤 큰거부터 하다가 마지막에 작은거 여러개 써야할 수도 있음 in3처럼
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    #DFS(0)
    a.sort(reverse = True)
    for i in a:
        x = m // i
        cnt += x
        m = m % i
        if m == 0:
            break
    print(cnt)

'''


