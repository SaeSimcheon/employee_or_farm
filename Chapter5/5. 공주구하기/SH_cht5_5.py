import sys
sys.stdin=open("input.txt", "r")
N,K = map(int,input().split())
print(N,K)

princes=list(range(1,N+1))

tail = princes
while len(tail)>1:
    if (len(tail) >= K) :
        head=tail[:K]
        head.pop()
        tail=tail[K:]
        tail.extend(head)
        #print(tail)
    else:
        if K % len(tail) ==0:
            tail.pop()
            continue
        else:
            print(tail)
            print(K)
            K_ = K % len(tail)
            print(K_)
            head=tail[:K_]
            head.pop()
            tail=tail[K_:]
            tail.extend(head)
            print(tail)


print(tail)



'''

import sys
from collections import deque

n,k= map(int,input().split())

dq = list(range(1,n+1))
print(dq)

dq = deque(dq)

while dq :
    for _ in range(k-1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq) == 1:
        print(dq[0])
        dq.popleft()




'''