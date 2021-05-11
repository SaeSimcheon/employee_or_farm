import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 


# 시간이 넘으면 return으로 가지를 끊으면 더이상 업데이트 되지 않고 멈춘다.
# 내가 틀렸던 이유 : 시간이 올라가는건 그 전에 가지에서 올라오는 건데 올라온 가지에 해당하는 시간이 업데이트 된다고 생각해서 그 스코어를 뺄 방법을 몰라서 틀림...

def DFS(L, sum, time):
    global res
    if time > m:
        return
    if L == n:
        if sum > res:
            res = sum
    else:
        DFS(L+1, sum + pv[L], time + pt[L])
        DFS(L+1, sum, time)
    

if __name__ == "__main__":
    n, m = map(int, input().split())
    pv = list()
    pt = list()
    for i in range(n):
        a, b = map(int, input().split())
        pv.append(a)
        pt.append(b)
    res = -2147000000
    DFS(0, 0, 0)
    print(res)



'''
def DFS(v, score, time):
    global res
    
    if time > m or v == n:
        score = score - q[v-1][0]
        if score > res:
            res = score
        return
        
    else:
        #ch[v] = 1
        DFS(v+1, score+q[v][0], time+q[v][1])
        #ch[v] = 0
        DFS(v+1, score, time)
        
    
                
            


if __name__ == "__main__":
    n, m = map(int, input().split())
    q = []
    for _ in range(n):
        a = list(map(int, input().split()))
        q.append(a)
    q.sort(reverse = True)
    time = 0
    res = 0
    ch = [0]*n

    DFS(0, 0, 0)
    print(res)

'''
