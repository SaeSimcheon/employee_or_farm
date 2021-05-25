import sys
from collections import deque
sys.stdin = open("input.txt","rt")

N = int(input())


seq=[0]*(N +1)

seq[1]=2
seq[2]=3

for i in range(3,N+1):
    seq[i]=seq[i-1] + seq[i-2]
    



print(seq[N])
