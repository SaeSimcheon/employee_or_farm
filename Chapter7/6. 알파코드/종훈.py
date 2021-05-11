import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 


# 상태트리 뻗을 때 26개의 가지를 뻗으면서 해당 숫자가 있으면 아래도 가지를 연결

def DFS(L, P):
    global cnt
    if L == n:
        cnt += 1
        for j in range(P):
            print(chr(res[j]+64), end = '')
        print()

    else:
        for i in range(1, 27):
            if code[L] == i:
                res[P] = i
                DFS(L+1, P+1)
            elif i >= 10 and code[L] == i//10 and code[L+1] == i%10: # 이부분에서 마지막 숫자가 1, 2일 경우 에러나서 insert -1 한거임.
                res[P] = i
                DFS(L+2, P+1)
            
    

if __name__ == "__main__":
    code = list(map(int, input())) # 숫자 하나씩 str로 끊어서 받음
    n = len(code)
    code.insert(n, -1) # 마지막에 -1 추가함, out of index range 대비
    res = [0] * (n+3)
    cnt = 0
    DFS(0, 0)
    print(cnt)


'''

# 이거 왜 돌아가는데 채점하면 exit_code_1 계속 나오지...?
# 아는 사람 손?

# 아스키코드 이용

def DFS(L):
    global cnt
    if L == a:
        cnt += 1
        for i in range(len(res)):
            print(chr(res[i]+64), end = '')
        print()
    else:
        if L<(a-1) and n[L+1] == '0':
            res.append(int(n[L:L+2]))
            DFS(L+2)
            res.pop()
        else:
            res.append(int(n[L]))
            DFS(L+1)
            res.pop()
            if L < (a-1) and (int(n[L:L+2]) < 27):
                res.append(int(n[L:L+2]))
                DFS(L+2)
                res.pop()

if __name__ == "__main__":
    n = input()
    a = len(n)
    res = list()
    cnt = 0
    DFS(0)
    print(cnt)
    
'''
