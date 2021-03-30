import sys
from collections import Counter

#sys.stdin=open('input.txt','rt')

n = int(input())


def price(n):
    money = list()
    for i in range(n):
        numbers = list(map(int, input().split()))
        counter = Counter(numbers)
        
        if max(map(int,counter.values())) == 3:
            money.append(10000+max(map(int,counter.keys()))*1000)
        elif max(map(int,counter.values())) == 2:
            money.append(1000+max(map(int,counter.keys()))*100)
        else :
            money.append(max(map(int,counter.keys()))*100)

print(price(n))
