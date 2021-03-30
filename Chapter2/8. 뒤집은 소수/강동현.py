'''
뒤집은 소수
'''
import sys


#sys.stdin = open("in2.txt","rt")


def reverse(x):
    x = x[::-1]
    return int(x)


def isPrime(x):
    if x == 1:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    else:
        return True


_ = input()
L = list(input().split())


for x in L:
    i = reverse(x)
    if isPrime(i):
        print(i,end = " ")
