import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 

###### BFS ########

# 노드의 레벨별로 탐색
# 큐 자료구조 이용

from collections import deque

MAX = 10000
ch = [0] * (MAX+1) # 갔던 곳을 다시 안가게 하기 위해 체크리스트 생성
dis = [0] * (MAX+1) # 해당 거리에 도착하기 위해 한 점프 횟수

n, m = map(int, input().split())
ch[n] = 1 # 시작지점 1로 변경 후 시작
dis[n] = 0

dq = deque()
dq.append(n)

while dq:
    now = dq.popleft()

    if now == m:
        break
    
    for next in(now-1, now+1, now+5):
        if 0 < next <= MAX:
            if ch[next] == 0:
                dq.append(next)
                ch[next] = 1
                dis[next] = dis[now] + 1

print(dis[m])
