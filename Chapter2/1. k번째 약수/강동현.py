'''
K 번째 약수
'''
import sys
#sys.stdin = open("input.txt","rt")


a = list(map(int,input().split()))


def f(N,K):
    RE = [x for x in range(1,N+1) if N % x == 0] 

    if len(RE) < K :
        return -1
    else :
        return RE[K-1]
    
print(f(a[0],a[1]))
