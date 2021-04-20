import sys

#sys.stdin=open('input.txt','rt')

n, m = list(map(int,input().split()))

answer = list(range(n))

def solution(n,m):
    res = n//m
    for i in range(1,res+1):
        answer.pop(i*m)
    return solution(n,m)

print(solution(n,m))

'''
큐 자료구조
-> 선입 선출 <-> 스택
-> deque
-> 양쪽에서 빼고 더할 수 있음

n, k = list(map(int,input().split()))

dq = list(range(1,n+1))

dq = deque(dq)
while dq:
    for _ range(k-1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq) == 1:
        print(dq[0])
        dq.popleft()



'''
