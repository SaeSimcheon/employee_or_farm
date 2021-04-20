import sys
#sys.stdin = open("input.txt", "rt")

##### 힙(heap) 자료구조 활용 #####
## heapq는 기본적으로 최소힙으로 작동
## 최대힙으로 작동하게 하려면 입력할 때 -부호를 붙여서 입력

import heapq as hq
a = []

while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(-hq.heappop(a)) # 출력할 때 원래 부호로 돌려놓기
    else:
        hq.heappush(a, -n) # 입력할 때 부호 -를 주고 입력
