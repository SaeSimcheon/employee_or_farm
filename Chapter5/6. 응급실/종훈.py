import sys
#sys.stdin = open("input.txt", "rt")

##### 큐 자료구조 활용 #####
## deque 라는 자료구조를 통해 적용
## deque : 앞뒤 둘다 뺐다 넣었다 할 수 있음
## appendleft, popleft / append, pop
from collections import deque

n, m = map(int, input().split())

# 튜플로 순서와 값을 같이 받아옴(list comprehension 이용)
Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q = deque(Q)

cnt = 0
while True:
    cur = Q.popleft()
    if any(cur[1] < x[1] for x in Q): # any : 단 한개라도 True이면 True를 return
        Q.append(cur)
    else: # 단 한개도 참이 아닐 경우 -> cur[1] 이 위험도가 가장 높다
        cnt += 1
        if cur[0] == m:
            break
print(cnt)


'''
### 내가 풀었다!!!!!!!!!!!!
n, m = map(int, input().split())
dq = list(map(int, input().split()))
dq = deque(dq)

cnt = 0
while True:
    # 밑에 while문은 가장 위험도 높은 환자 1명이 진료를 받는 알고리즘
    while dq[0] != max(dq):
        dq.append(dq.popleft())
        # m이 제일 앞이면 맨 뒤로 가야하니까 숫자 바꿔주고 아니면 -1
        if m == 0:
            m = len(dq) - 1
        else:
            m -= 1

    if m == 0: # m번째 환자가 진료를 받는 경우 break
        cnt += 1
        print(cnt)
        break
    else: # 다른 환자가 진료를 받는 경우 그 환자를 목록에서 제거하고 cnt +1 하고 계속
        dq.popleft()
        m -= 1
        cnt += 1

'''