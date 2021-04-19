import sys
#sys.stdin = open("input.txt", "rt")
'''n, k = map(int, input().split())
from collections import deque
a = range(1,n+1)
a = deque(a)
while len(a)>1:
    a.rotate(-(k-1))
    a.popleft()
print(a[0])'''

# 첫시도 100
# deque.rotate(n): n만큼 재배열해주는 함수
# 재배열을 해야할거 같은데 고민하다가 검색해서 찾음
# 이거쓰니까 쉽게 풀었다.

# que는 first in first out(먼저 들어간게 먼저 나온다)
# que 자료구조는 deque library를 사용! list와 pop/append는 동일
# but 왼쪽에서도 꺼내고 빼기 가능(popleft/appendleft)
from collections import deque
n, k = map(int, input().split())
dq = list(range(1,n+1))
dq = deque(dq)
while dq:
    for _ in range(k-1): #변수없이 반복문만 돌기 때문
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq)==1:
        print(dq[0])
        dq.popleft()

# 배운점
# 1. deque를 사용한 que 자료구조 : First in, first out(먼저 들어간게 먼저 나온다)
# 2. que 자료구조는 deque library를 사용! list와 pop/append는 동일
# but 왼쪽에서도 꺼내고 빼기 가능(popleft/appendleft)
# 3. deque.rotate(n): n만큼 재배열해주는 함수, n>0 이면 오른쪽으로 이동 n<0이면 왼쪽으로 이동
