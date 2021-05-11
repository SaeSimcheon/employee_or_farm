'''
동전교환
'''
import sys


n = int(input())
arr = list(map(int,input().split()))
m = int(input())

'''
n,m = 3,15
arr = [1,2,5]
'''

dy = [0] * (m+1)

for i in range(1,m+1):
    post = [i-tmp for tmp in arr if i-tmp >= 0]

    if len(post) == 0 :
        continue
    else:       
        dy[i] = min([dy[x] for x in post]) + 1


print(dy[-1])
