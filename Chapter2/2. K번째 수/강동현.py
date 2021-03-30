'''
K 번째 수

'''
import sys

#sys.stdin = open("in1.txt","rt")


T = int(input())

for i in range(T):
    n, s, e, k = map(int,input().split())
    ll = list(map(int,input().split()))
    ll = ll[s-1:e]
    ll.sort()
    print("#" + str(i+1) + str(ll[k-1]))
