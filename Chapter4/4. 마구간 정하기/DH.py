'''
마구간 정하기(결정알고리즘)

pick : 거리가 주어졌을 때 넣을 수 있는 말의 수

말의 좌표 중복 x >> lt = 1부터 시작 가능
'''
import sys


#sys.stdin = open("in1.txt","r")

n,c = map(int,input().split())
arr = [int(input()) for x in range(n)]
'''
n,c = 5,3
arr = [1,2,8,4,9]
'''
arr.sort()


rt = arr[-1] - arr[0]
lt = 0

def pick(arr,v):

    F = arr[0]
    c = 1
    for i in arr[1:]:
        if i - F >= v:
            c += 1
            F = i
    return c

ans = 0

if c == 2 :
    print(rt)
else:
    while rt > lt:

        mid = (rt + lt)//2
#        print(mid)
        re = pick(arr,mid)

        if re >= c :
            ans = mid
            lt = mid + 1
        else :
            rt = mid 
            
    print(ans)
