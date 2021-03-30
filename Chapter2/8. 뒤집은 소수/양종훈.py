import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

def reverse(x):
    s = str(x)[::-1]
    
    return int(s)

def isPrime(x):
    cnt = 0
    for i in range(1,x+1):
        if x%i == 0:
            cnt += 1
    if cnt == 2:
        return True
    else:
        return False


for i in range(n):
    if isPrime(reverse(a[i])) == True:
        print(reverse(a[i]), end = " ")