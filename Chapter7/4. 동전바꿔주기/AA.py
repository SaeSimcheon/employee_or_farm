import sys
#sys.stdin=open('input.txt','rt')

##n트리

input = sys.stdin.readline #입력 양이 많을 때 속도가 빨라지기 위해

# text 읽을 때는 s = input().rstrip()

def DFS(L,many,money):
    global weights
    global p
    if money > p :
        return
    if L == c:
        if money == p:
            m.append(money)
        #return
    else:
        for i in range(a[L][1]+1):
            #m.append(money)
            DFS(L+1,i,money+a[L][0]*(i))

if __name__=="__main__":
    p = int(input())
    c = int(input())
    a = list()
    for _ in range(c):
        a.append(list(map(int, input().split())))
    a.sort(reverse=True)
    m = list()
    DFS(0,0,0)
    print(m.count(p))
    #print(m)
