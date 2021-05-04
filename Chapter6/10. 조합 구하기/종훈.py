import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 

########### 이진트리 순회 : 깊이 우선 탐색(DFS) ###############


# 풀이 보니까 s자리에 (i+1)해야하는데 난 (s+i) 했네...
# 똑바로 나오니까 맞는 줄 알았지 ㅡㅡ

def DFS(L, s):
    global cnt
    if L == m:
        for j in range(m):
            print(res[j], end = ' ')
        cnt += 1
        print()
    else:
        for i in range(s, n+1):
            res[L] = i
            DFS(L+1, i+1)
    
        
            

if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt = 0
    res = [0] * (n+1)
    DFS(0, 1)
    print(cnt)



'''
# 이것도 40점 망할..
def DFS(L, s):
    global cnt
    if L == m:
        for i in range(m):
            print(res[i], end = ' ')
        print()
        cnt += 1
        return
    if s > n:
        return
    else:
        for i in range(s, n+1):
            res[L] = i
            DFS(L+1, s+i)
        
            

if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt = 0
    res = [0] * m
    ch = [0] * (n+1)
    DFS(0, 1)
    print(cnt)
'''
    

'''
# 40점...
def DFS(L):
    global a
    global cnt
    if L == m:
        for i in range(m):
            print(res[i], end = ' ')
        print()
        cnt += 1
    else:
        for i in range(a, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                DFS(L+1)
                ch[i] = 0
        else:
            a += 1
            

if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt = 0
    res = [0] * m
    ch = [0] * (n+1)
    a = 1
    DFS(0)
    print(cnt)
'''
