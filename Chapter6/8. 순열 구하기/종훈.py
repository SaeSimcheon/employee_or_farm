import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 

########### 이진트리 순회 : 깊이 우선 탐색(DFS) ###############


### 중복순열에서 checklist를 만들어서 그 가지는 뻗지 못하도록 한다.

# 답이랑 내꺼랑 토씨 하나 안틀리고 똑같네;;

def DFS(L):
    global cnt
    if L == m:
        for j in range(L):
            print(res[j], end = ' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                DFS(L+1)
                ch[i] = 0
            else:
                pass
            

if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    ch = [0]* (n+1)
    cnt = 0
    DFS(0)
    print(cnt)



'''
# 설명듣고 내가 짠 것
def DFS(L):
    global cnt
    if L == m:
        
        for j in range(m):
            print(res[j], end = ' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                DFS(L+1)
                ch[i] = 0
            else:
                pass
            

if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    ch = [0]* (n+1)
    cnt = 0
    DFS(0)
    print(cnt)
'''
    

