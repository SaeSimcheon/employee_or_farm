# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 15:57:01 2021

@author: Park Jung Hoon
"""



import os
import sys

n,k = map(int, input().split())
count = 0
numbers = []

for i in range(1,n+1):
    if n%i ==0:
        count += 1
        numbers.append(i)
    if k == count:
        print(i)
else :
    print(-1)

assert k < count, '약수가 더 적어요'

print(numbers[k])
