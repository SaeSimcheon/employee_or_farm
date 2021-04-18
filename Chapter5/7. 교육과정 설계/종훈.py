import sys
#sys.stdin = open("input.txt", "rt")

##### 큐 자료구조 활용 #####
## deque 라는 자료구조를 통해 적용
## deque : 앞뒤 둘다 뺐다 넣었다 할 수 있음
## appendleft, popleft / append, pop
from collections import deque




need = input()
n = int(input())

# 자료 받아오는 것과 검증을 동시에 진행
for i in range(n):
    plan = input()
    dq = deque(need)

    for x in plan: # str 로 받은 input은 굳이 list로 만들지 않아도 for문 적용시 하나하나
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq) == 0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))


'''
## 결국 실패...

level = input()
level = [level[i] for i in range(len(level))]
level = deque(level)
#print(level)

n = int(input())

a = []
for _ in range(n):
    b = input()
    b = [b[i] for i in range(len(b))]
    a.append(b)


for i in range(n):
    for x in a[i]:
        if x in level:
            if x == level[0]:
                level.popleft()
                if len(level) == 0:
                    print("#%d YES" %(i+1))
                    break
            else:
                print("#%d NO" %(i+1))
                break
        else:
            continue
'''

'''
## 큐 자료구조 안쓰고 풀어본 것
# 한 수업이 여러번 있을 경우 성립 안됨

level = input()
level = [level[i] for i in range(len(level))]
#print(level)

n = int(input())

a = []
for _ in range(n):
    b = input()
    b = [b[i] for i in range(len(b))]
    a.append(b)
#print(a)

for i in range(n):
    check = []
    for j in range(len(level)):
        l = a[i].index(level[j])
        check.append(l)

    if check == sorted(check):
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))
'''