'''
창고 정리

답 : 굳이 index 찾지 말고 sort
'''

import sys

#sys.stdin = open("in1.txt","r")

'''
L = 10
arr = [69,42,68,76,40,87,14,65,76,81]
m = 50
'''

_ = input()
arr = list(map(int,input().split()))
m = int(input())
i = 0

while 1:
    max_idx = arr.index(max(arr))
    min_idx = arr.index(min(arr))

    arr[max_idx] -=1
    arr[min_idx] +=1

    i +=1
    if i == m:
        break
print(max(arr)-min(arr))
