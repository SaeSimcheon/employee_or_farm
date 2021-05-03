'''
동전교환

ㄲㅂ
ll.sort()

a = 0

while m > 0 :
    if m < ll[-1]:
        ll.pop()
    else:
        m -= ll[-1]
        a += 1
print(a)
'''

import sys

#sys.stdin = open("in4.txt","r")

_ = input()
ll = list(map(int,input().split()))
m = int(input())

ll.sort(reverse = True)
'''
ll = [1,2,5]
m = 15
'''
ans = 500
def DFS(m,num):
    global ll,ans

    if m < 0 or num > ans :
        return

    else:
        for i in ll:
            if m - i == 0 :
                if ans > num +1:
                    ans = num +1
            else:
                DFS(m-i,num+1)

DFS(m,0)
print(ans)
