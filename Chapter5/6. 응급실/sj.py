import sys
#sys.stdin = open("input.txt", "rt")
'''n, m = map(int, input().split())
a = list(map(int, input().split()))
from collections import deque
a = deque(a)
a_num = deque(range(n))
b = []
b_num = []
while len(a) > 0:
    if a[0] != max(a):
        a.rotate(-1)
        a_num.rotate(-1)
    else:
        c = a.popleft()
        d = a_num.popleft()
        b.append(c)
        b_num.append(d)
for idx, i in enumerate(b_num):
    if i == m:
        print(idx+1)'''

# 첫시도 100
# deque를 활용했는데, index도 같은 순서대로 진행을 해서
# m번째 환자가 어디에 위치한지 알 수 있도록
# 진료 안받으면 같이 rotate시키고, 받으면 같이 pop해서 append하는 식으로
# 마지막에는 m번쨰 환자가 언제 진료받았는지 enumerate로 idx 불러왔음

from collections import deque
n, m = map(int, input().split())
Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
# 인덱스와 값을 한번에 input 시키는 방법 / 리스트 안에는 tuple(idx, val)로 이루어져 있다
Q = deque(Q)
cnt = 0
while True:
    cur = Q.popleft()
    if any(cur[1]<x[1] for x in Q):
        Q.append(cur)
    else:
        cnt+=1
        if cur[0]==m:
            break
print(cnt)

# 느낀점
# 1. while을 굳이 다 돌릴 필요는 없겠구나,,, 적절히 break를 걸어주는게 필요할듯
# 2. 근데 답안이 간단하긴 한데, 왜 어렵게 짠거 같냐

# 배운점
# 1. 인덱스와 값을 한번에 input 시키는 방법 / 리스트 안에는 tuple(idx, val)로 이루어져 있다
# Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
# 2. any() : 하나라도 만족하면 True / 안에 for로 iterable을 줄 수 있음
