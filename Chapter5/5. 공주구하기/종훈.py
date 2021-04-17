import sys
#sys.stdin = open("input.txt", "rt")

##### 큐 자료구조 활용 #####
## deque 라는 자료구조를 통해 적용
## deque : 앞뒤 둘다 뺐다 넣었다 할 수 있음
## appendleft, popleft / append, pop
from collections import deque

n, k = map(int, input().split())
dq = list(range(1, n+1))
dq = deque(dq)

while dq:
    for _ in range(k-1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq) == 1:
        print(dq[0])
        dq.popleft() # break 할 수도 있지만 비워버려서 while문 조건 만족시켜서 끝냄


'''
# 코드 설명 안보고 개념만 보고 푼 풀이
n, k = map(int, input().split())

pr = [x for x in range(1, n+1)]

#print(pr)
lst = []

while len(pr) > 1:

    for _ in range(k-1):
        pr.append(pr.pop(0))
    pr.pop(0)
print(pr[0])
'''