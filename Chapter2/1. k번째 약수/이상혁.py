
import sys
#sys.stdin = open("input.txt","rt")

N ,K = map(int,input().split(","))

out = list()
if N == K:
    print(N)
else:
    
    for i in range(int(N)):
        if N % (i + 1) == 0 :
            out.append(i+1)
    
if len(out) < K :
    print(-1)
else:
    print(out[K-1])
