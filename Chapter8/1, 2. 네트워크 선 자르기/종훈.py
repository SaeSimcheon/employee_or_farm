import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 

################ 동적 계획법 #################

##### Top-Down #####
# 메모이제이션 : 재귀호출의 경우 미리 구해진 것을 기록을 해서 다음 호출됐을 때 cut-edge를 해버린다.

def DFS(len):
    if dy[len] > 0: # 메모이제이션 활
        return dy[len]
    if len == 1 or len == 2:
        return len # 길이가 1일 경우 자르는 방법이 1가지 방법/ 2일 경우 2가지 방법이라서
    else:
        dy[len] = DFS(len-1) + DFS(len-2)
        return dy[len]

if __name__ == "__main__":
    n = int(input())
    dy = [0] * (n+1)
    print(DFS(n))



##### Bottom-Up #####

n = int(input())
dy = [0] * (n+1)
dy[1] = 1
dy[2] = 2

for i in range(3, n+1):
    dy[i] = dy[i-1] + dy[i-2]

print(dy[n])





'''
# 오 DFS로 하니까 Time limit 걸림
def DFS(l, v):
    global cnt
    if v < 0 :
        return
    if v == 0:
        cnt += 1
    else:
        DFS(1, v-1)
        DFS(2, v-2)


if __name__ == "__main__":
    n = int(input())
    cnt = 0
    #DFS(0, n)
    DFS(1, n-1)
    DFS(2, n-2)
    print(cnt)
'''
