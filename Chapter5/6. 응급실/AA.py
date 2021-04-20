import sys
from collections import deque
#sys.stdin=open('input.txt','rt')

'''
n, m = map(int,input().split())
hazard = list(map(int,input().split()))

hazard = deque(hazard)

count = 1

while index:
    cur = hazard.popleft()
    if cur == max(hazard):
        hazard = hazard
    else :
        hazard.append(cur)
        count += 1

print(count)

'''
'''
n, m = map(int,input().split())
hazard = list(map(int,input().split()))
patient = hazard[m]
count = 0
for i in range(m):
    if hazard[i] == patient:
        count += 1
hazard.sort(reverse = True)
print(hazard.index(patient)+1+hazard.count(patient))
'''

n, m = map(int,input().split())
hazard = [(pos, val) for pos, val in enumerate(list(map(int,input().split())))]
hazard = deque(hazard)
cnt = 0
while True:
    cur=hazard.popleft()
    if any(cur[1]<x[1] for x in hazard):
        hazard.append(cur)
    else:
        cnt+=1
        if cur[0] == m:
            break

print(cnt)





