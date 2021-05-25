import sys
from collections import deque
sys.stdin = open("input.txt","rt")

N = int(input())
seq=[list(map(int,input().split())) for _ in range(N)]

print(seq)

dx = [0,1]
dy = [1,0]

spot = [0,0]


que = deque()
result = deque()
que.append(spot)

result.append(seq[0][0])
out = list()


while que:
    element = que.popleft()
    result_element=result.popleft()
    
        
    for i in range(2):
        xx =element[0] + dx[i]
        yy =element[1] + dy[i]
        
        if not (xx < N and yy < N ):
            continue
        que.append([xx,yy])
        result.append(result_element + seq[xx][yy])
        
        if xx == N-1 and yy == N-1:
            out.append(result_element + seq[xx][yy])
    
        
    
            
        
print((out))