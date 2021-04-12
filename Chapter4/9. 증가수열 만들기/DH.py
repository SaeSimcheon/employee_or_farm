'''
증가수열 만들기(그리디)
'''

import sys


#sys.stdin = open("in1.txt","r")

'''
n = 5
arr = [2,4,5,1,3]

'''
_ = input()
arr = list(map(int,input().split()))

a = [0]

ans = ""

while 1:
    if arr[0] > a[-1]:
        if arr[-1] > a[-1]:
            if arr[-1] < arr[0]:
                a.append(arr.pop())
                ans += "R"

            else:
                a.append(arr.pop(0))
                ans += "L"

        else:
            a.append(arr.pop(0))
            ans += "L"
    else:
        if arr[-1] > a[-1]:
            a.append(arr.pop())
            ans += "R"
        else:
            break

    if len(arr) == 1:
        if arr[0] > a[-1]:
            a += arr[0]
            ans += "L"
            break
        else:
            break

print(len(a)-1,ans,sep = "\n")

