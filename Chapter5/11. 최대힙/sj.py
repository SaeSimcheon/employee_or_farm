import sys
#sys.stdin = open("input.txt", "rt")
import heapq as hq
a=[]
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a)==0:
            print(-1)
        else:
            print(-hq.heappop(a))
    else:
        hq.heappush(a,-n)

# 첫시도 100
# heap에 접근할때 최솟값만 표기하는데, 이걸 이용해서
# push를 음수로 바꾸고 결과값을 다시 양수로 바꾸면 그게 최대값