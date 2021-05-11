import sys
#.stdin=open('input.txt','rt')

##n트리

input = sys.stdin.readline #입력 양이 많을 때 속도가 빨라지기 위해

# text 읽을 때는 s = input().rstrip()

def DFS(L,P):
    global cnt
    if L==n:
        cnt+=1
        for j in range(P):
            print(chr(res[j]+64), end='')
        print()

    else:
        for i in range(1,27):
            if code[L]==i:
                res[P]=i
                DFS(L+1,P+1)
            elif i>=10 and code[L]==i//10 and code[L+1]==1%10 :
                res[P]=i
                DFS(L+2,P+1)
                

if __name__=="__main__":
    code = list(map(int,input()))
    n = len(code)
    code.insert(n,-1)
    res=[0]*(n+3)
    cnt=0
    DFS(0,0)
    print(cnt)
    
