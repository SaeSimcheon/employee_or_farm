'''
K 번째 큰 수

중복제거

'''
import sys

#sys.stdin = open("in2.txt","rt")


from itertools import combinations

n,k = map(int,input().split())
L = list(map(int,input().split()))

L = list(combinations(L,3))
L = list(set([sum(x) for x in L]))

L.sort()
#print(L)
print(L[-k])

