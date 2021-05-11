import sys
from collections import deque
#sys.stdin = open("input.txt", "rt")
# BFS 는 넓이우선탐색, 레벨마다 탐색을 한다
# 자료구조는 que / first in first out
# 레벨마다 que에 넣고 leftpop해서 탐색 반복

maximum = 100000
ch = [0] * (maximum+1)
dis = [0] * (maximum+1)
n, m =map(int,input().split())
ch[n]=1  #첫 출발에 표시
dis[n]=0
dQ = deque()
dQ.append(n)
while dQ:
    now = dQ.popleft()
    if now==m:
        break
    for next in (now-1, now+1, now+5): # next가 tuple 값을 하나씩 돈다
        if 0<next<=maximum:
            if ch[next]==0:
                dQ.append(next)
                ch[next]=1
                dis[next]=dis[now]+1
print(dis[m])

# 배운점
# 1. BFS
# BFS는 최단거리를 구할 때 사용한다.
# 대략적인 구현 방법은 deque의 초기값으로 출발점을 넣고 pop한 뒤,
# pop한 점에서 한번에 갈 수 있는 도착점들을 deque에 순서대로 넣는다.
# 이 때 도착점들은 방문한 적이 없는 상태일 때만 deque에 넣는다.
# 넣었다면 방문한 것을 체크해준다.
# 그리고 거리는 출발점을 0으로 두고 pop한 점의 거리에 +1을 해준다.