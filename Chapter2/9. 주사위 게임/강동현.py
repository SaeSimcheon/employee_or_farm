'''
주사위 게임

'''
import sys
#sys.stdin = open("in1.txt","rt")

N = int(input())

RE = 0
for i in range(N):
    A = list(map(int,input().split()))
    B = list(set(A))

    if len(B) == 3:
        Can = max(A) * 100
    elif len(B) == 2:
        if A.count(B[0]) == 2:
            Can = B[0] * 100 + 1000
        else:
            Can = B[1] * 100 + 1000
    else :
        Can = 10000 + B[0] * 1000

    if Can > RE:
        RE = Can
        
print(RE)
