'''
침몰하는 타이타닉(그리디)

sort 하고 앞뒤로 더한 값이 제한보다 크면 뒤에 값 pop
아니면 같이 pop

list pop vs deque pop

앞뒤로 pop 할때는 deque가 더 빠름 (중간 pop 안됨)
'''

import sys

#sys.stdin = open("in1.txt","r")

'''
n,m = 5,140
arr = [90,50,70,100,60]


'''
n,m = map(int,input().split())
arr = list(map(int,input().split()))


arr.sort()

ans = 0
while arr:
    if arr[0] + arr[-1] > m:
        arr.pop()
        ans += 1
    else :
        arr.pop()
        arr.pop(0)
        ans += 1
    if len(arr)==1:
        arr.pop()
        ans += 1
        
print(ans)
