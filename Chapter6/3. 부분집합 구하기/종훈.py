import sys
#sys.stdin = open("input.txt", "rt")


########### 이진트리 순회 : 깊이 우선 탐색(DFS) ###############



def DFS(v):
    if v == n+1:
        for i in range(1, n+1):
            if ch[i] == 1:
                print(i, end = " ")
        print()
        return
    else:
        ch[v] = 1
        DFS(v+1)
        ch[v] = 0
        DFS(v+1)



if __name__ == "__main__":
    n = int(input())
    ch = [0] * (n+1)
    DFS(1)



'''
# 상태트리 구성을 잘못함
def DFS(v):
    if v > n:
        
        return
    else:
        #print(v, end = ' ') 
        DFS(v+1)
        #print(v, end = ' ')
        DFS(v+2)
        print(v)



if __name__ == "__main__":
    n = int(input())

    for i in range(1, n+1):
        DFS(i)
'''