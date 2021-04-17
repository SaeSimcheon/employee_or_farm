'''
최소힙
'''
import heapq
import sys

#sys.stdin = open("in1.txt","r")
a = []
while 1:
    n = int(input())

    if n == -1 :
        break

    if n == 0:
        print(heapq.heappop(a))

    else:
        heapq.heappush(a,n)




