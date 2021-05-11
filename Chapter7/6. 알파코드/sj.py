import sys
#sys.stdin = open("input.txt", "rt")
'''def DFS(L,s):
    global cnt
    if L==n:
        print(res)
        for j in range(s):
            print(chr(res[j]+64), end = '')
        print()
        cnt+=1
    else:
        for i in range(1,27):
            if num[L]==i:
                res[s]=i
                DFS(L+1,s+1)
            elif i>=10 and num[L]==i//10 and num[L+1]==i%10:
                res[s]=i
                DFS(L+2,s+1)

if __name__=="__main__":
    num = list(map(int, input()))
    n = len(num)
    res = [0]*n
    cnt = 0
    DFS(0,0)
    print(cnt)'''

# 모르겠따
# 설명 듣고도 비슷한데 뭘 놓친건지 모르겠음

def DFS(L, P):
    global cnt
    if L==n:
        cnt+=1
        for j in range(P):
            print(chr(res[j]+64), end = '')
        print()
    else:
        for i in range(1,27):
            if code[L]==i:
                res[P]=i
                DFS(L+1, P+1)
            elif i>=10 and code[L] == i//10 and code[L+1] == i%10:
                res[P]=i
                DFS(L+2, P+1)

if __name__ == "__main__":
    code = list(map(int, input()))
    n = len(code)
    code.insert(n, -1) # 두자리수 확인할때 마지막 인덱스에서 이거 없으면 out of range
    res = [0]*(n+3)
    cnt = 0
    DFS(0, 0)
    print(cnt)


# 마지막 부분 설명이 뭔소린지 모르겠음
# res는 일부러 많이 늘린건가?