'''
응급실

pop 하고 위험도 높은 환자 있는지 확인 >> 없으면 num += 1 이 환자가 M번째 환자였으면 break
                                      >> 있으면 push
'''
import sys

n,k = map(int,input().split())
arr = list(map(int,input().split()))

#n,k = 6,0
#arr = [60,60,90,60,60,60]
#n,k = 5,2
#arr = [60,50,70,80,90]
arr = [[x,idx] for idx,x in enumerate(arr)]

num = 0
while 1:
    temp = arr.pop(0)

    F = [True for x in arr if x[0] > temp[0]]

    if len(F) != 0:
        arr += [temp]

    else :
        num += 1
        if temp[1] == k:
            break
    
print(num)
