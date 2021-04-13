import sys
#sys.stdin = open("input.txt", "rt")

n, limit = map(int, input().split())
p = list(map(int, input().split()))

p.sort()
cnt = 0

while p:
    if len(p) == 1: # 마지막 한명 남았을 경우
        cnt += 1
        break

    if p[0] + p[-1] > limit:
        p.pop() # 맨 뒷사람(제일 무거운 사람) 혼자 타고 나감
        cnt += 1
    else:
        p.pop(0) # 맨 앞 제거
        p.pop() # 맨 뒤 제거
        cnt += 1

print(cnt)

### list 의 경우 pop(0)을 할 경우 뒤에 자리가 한칸씩 앞으로 오는 연산을 진행 -> 비효율
### deque라는 자료구조는 단순히 넣었다 빼기만, 자료가 이동하지 않는다. 자료를 뺄 경우 그 다음 것을 가리킴

from collections import deque
n, limit = map(int, input().split())
p = list(map(int, input().split()))

p.sort()
p.deque(p)
cnt = 0

while p:
    if len(p) == 1: 
        cnt += 1
        break

    if p[0] + p[-1] > limit:
        p.pop() 
        cnt += 1
    else:
        p.popleft() # 이부분에서 차이가 생김
        p.pop() 
        cnt += 1

print(cnt)


'''
n, m = map(int, input().split())
weight = list(map(int, input().split()))

weight.sort(reverse = True)

boat = 0

for i in range(n):
    if i >= len(weight):
        break
    for j in range(i+1, len(weight)):
        if weight[i] + weight[j] <= m:
            boat += 1
            del weight[j]
            break
    else:
        boat += 1
print(boat)
'''