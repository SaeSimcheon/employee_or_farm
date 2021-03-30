'''
에라토스테네스 체
'''
import sys
from math import ceil

#sys.stdin = open("in1.txt","rt")


def ch(x):
    R = [True] * (x+1)

    for i in range(2,x//2):
        if R[i] == True:
            
            for num in range(i+i,x+1,i):
                R[num] = False
    return sum(R)-2


n = int(input())

print(ch(n))
