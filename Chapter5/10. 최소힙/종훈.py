import sys
#sys.stdin = open("input.txt", "rt")

##### 힙(heap) 자료구조 활용 #####

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
            print(hq.heappop(a)) # hq.heappop(list) : heap 구조에서 root node 값 return
    else:
        hq.heappush(a, n) # hq.heappush(lisn, value) : list에 최소힙 형태로 n을 push