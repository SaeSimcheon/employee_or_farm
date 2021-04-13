import sys

#sys.stdin=open('input.txt','rt')

n , m = map(int,input().split())

people = list(map(int,input().split()))

people.sort()

cnt = 0
sum = 0
'''
for i in range(n):
    length = len(people)
    sum = people[length-1] + people[i]
    if sum <= m :
        cnt += 1
        sum = 0
        people.pop(length)
    else :
        cnt += 1
        sum = 0
        people.pop(i)
'''

while len(people) > 0 :
    length = len(people)
    sum = people[0] + people[-1]
    if sum > m:
        cnt += 1
        people.pop()
    else :
        people.pop(0)
        people.pop()
        cnt += 1


print(cnt)
#60



'''
from collections import deque


n , m = map(int,input().split())

people = list(map(int,input().split()))

p = deque(p)

while p:
    if len(p)==1:
        cnt += 1
        break
    if p[0] + p[-1] > m:
        p.pop()
        cnt += 1
    else:
        p.plpleft()
        p.pop()
        cnt += 1

print(cnt)

'''
