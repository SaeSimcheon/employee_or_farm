import sys
import re

#sys.stdin=open('input.txt','rt')

n = int(input())

numbers = list(map(int, input().split()))
reverse_numb = list()

def reverse(x):
    x = str(x)
    tmp = ''
    for char in x:
        tmp = char + tmp
    for i in range(0,len(tmp)):
        if re.search(r'[0]+',tmp[i]):
            tmp = tmp[1:len(tmp)]
        else :
            return int(tmp)

for number in numbers:
    reverse_numb.append(reverse(number))


def isPrime(x):
    tmp = 0
    for i in range(2,x//2):
        res = x%i
        if res==0:
            tmp = 1
        else :
            tmp = tmp
    if tmp == 0:
        return x

answer = list()
for number in reverse_numb:
    answer.append(isPrime(number))

answer = list(filter(None,answer))


print(answer)

'''
import sys
import re

#sys.stdin=open('input.txt','rt')

def reverse(x):
    res = 0
    while x>0:
        t = x%10
        res = res*10 + t
        x = x//10
    return res

def isPrime(x):
    if x ==1 :
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    else:
        return True

n = int(input())

a = list(map(int, input().split()))
for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')
'''



