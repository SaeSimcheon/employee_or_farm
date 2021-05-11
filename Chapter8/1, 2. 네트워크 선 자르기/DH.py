'''
동적계획법이란?
fibonacci 수열

import sys
#sys.stdin = open("in1.txt")
n = int(input())

dy = [0,1,2] + [0] * n


for i in range(3,n+1):
    dy[i] = dy[i-1] + dy[i-2]
print(dy[n])
'''


'''
가지 수 줄이기 >> 계산한 값을 저장하는 것이 중요

import sys
n = int(input())


def ans(num):

    if num <= 2:
        return num
    else:
        return ans(num-1) + ans(num-2)

print(ans(n))




import sys
n = int(input())
def ans(num):

    if num == 1 or num == 2:
        return num

    if dy[num] > 0 :
        return dy[num]

    else:
        dy[num] = ans(num - 1) + ans(num - 2)
        return dy[num]



dy = [0] * (n+1)
print(ans(n))
#print(dy)
'''


