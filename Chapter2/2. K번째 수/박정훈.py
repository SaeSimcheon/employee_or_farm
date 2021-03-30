
import os
import sys

T = int(input())

for i in range(T):
    n,s,e,k = map(int, input().split())
    l = list(map(int, input().split()))
    l = sort(l[s-1:e])
    print('#%d, %d'%(i+1, l[k-1]))

'''
def solution(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    T = content[0]
    for i in range(T):
        n,s,e,k = map(int,content[2*T+1])
        l = list(map(int, content[2*T+2].split()))
        l = l[s-1:e]
        print("#",i+1,l[k])
'''
