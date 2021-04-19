import sys
#sys.stdin = open("input.txt", "rt")
'''def eliminate(x):
    x = list(x)
    i = 0
    while i < len(x):
        for j in range(len(x)-1,i,-1):
            if x[j] == x[i]:
                x.pop(j)
        i += 1
    x = ''.join(x)
    return x
required = input()
n = int(input())
design = []
for i in range(n):
    design.extend(input().split())
for i in range(n):
    a = ''
    for j in design[i]:
        for k in range(len(required)):
            if j == required[k]:
                a += j
    if eliminate(a) == required:
        print("#%d" %(i+1),"YES")
    else:
        print("#%d" %(i+1),"NO")'''

# 첫시도 100
# 근데 큐를 안쓰고 풀었다 / 큐쓰고도 풀어봐야겠다
# 처음에 eliminate로 중복문자열 제거하는 함수 만들고
# required에 맞는 문자열만 뽑아내고, 비교해서 프린트

'''required = input()
n = int(input())
from collections import deque
for i in range(n):
    design = input()
    a = deque(required)
    for j in design:
        if j in a:
            if j != a.popleft():
                print("#%d" %(i+1),"NO")
    else:
        if len(a)==0:
            print("#%d" %(i+1),"YES")'''

# 두번째 20
# 큐를 쓰니까 4개가 틀림 / 왜 틀린거지
'''required = input()
n = int(input())
from collections import deque
for i in range(n):
    design = input()
    a = deque(required)
    for j in design:
        if j in a:
            if j != a.popleft():
                print("#%d" %(i+1),"NO")
                break
    else:
        if len(a)==0:
            print("#%d" %(i+1),"YES")
        else:
            print("#%d" %(i+1),"NO")'''

# 세번째 100
# 마지막에 NO가 출력이 안되는경우가 있길래 이거도 고려
# 중간 if문에서도 두번 출력이 되서 break
from collections import deque
need = input()
n = int(input())
for i in range(n):
    plan = input()
    dq = deque(need)
    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" % (i + 1))
                break
    else: #앞 for문에서 break에 안걸리면 정상적으로 돈거니까
        if len(dq)==0:
            print("#%d YES" % (i + 1))
        else:
            print("#%d NO" % (i + 1))

# 느낀점
# 1. 항상 풀기전에 문제 시뮬레이션을 잘 짜야겠다 / 답의 경우의수를 잘 고려해야함함

