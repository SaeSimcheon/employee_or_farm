import sys
#sys.stdin = open("input.txt", "rt")

#### 재귀함수와 스택 ####

def DFS(x):
    if x == 0:
        return
    else:
        DFS(x//2) # 거꾸로 출력하기 위해 print 앞으로 옮겨줌
        print(x%2, end = '')
        #DFS(x//2)

if __name__ == "__main__":
    n = int(input())
    DFS(n)




# 100점
'''
n = int(input())
lst = list(range(10))
lst = lst[::-1]
#print(lst[::-1])


def DFS(x):
    res = 0
    for i in lst:
        a = x // (2 ** i)
        b = x % (2 ** i)
        x = b
        res = res + a*(10**i)
    return res

print(DFS(n))
'''