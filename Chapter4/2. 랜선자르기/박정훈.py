import sys

#sys.stdin=open('input.txt','rt')

k, n = map(int,input().split())

numbers = list()

for i in range(k):
    numbers.append(int(input()))
    
'''
lt = 0

rt = min(numbers)-1

mid = (lt+rt)//2

def find_answer(n,lt,rt,mid):
    interval = list(range(n))
    candidate = interval[mid]
    count = 0
    for i in range(len(numbers)):
        count += numbers[i]//candidate
    if count > k :
        lt = mid + 1
        rt = rt
        mid = (lt+rt)//2
        return lt, rt, mid

    elif count < k :
        lt = lt
        rt = mid - 1
        mid = (lt+rt)//2
        return lt,rt, mid

    else :
        return lt,rt,mid


while lt <= rt :
    lt,rt,mid = find_answer(min(numbers),lt,rt,mid)

print(list(range(min(numbers)))[mid])
'''

Line = []

res = 0

def count(len):
    cnt=0
    for x in Line:
        cnt += (x//len)
    return cnt


for i in range(k):
    Line.append(int(input()))
    largest = max(Line)

lt = 1
rt = largest

while lt <= rt:
    mid = (lt+rt)//2
    if count(mid) >= n:
        res = mid
        lt = mid + 1
    else :
        rt = mid - 1

print(res)















