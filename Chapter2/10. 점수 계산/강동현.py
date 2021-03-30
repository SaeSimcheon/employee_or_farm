'''
점수 계산
'''
import sys
#sys.stdin = open("in1.txt","rt")

_ = input()
L = list(map(int,input().split()))

ANS = 0
score = 0 

'''
for i in L:
    if i == 0:
        score = 0
    else :
        if score == 0:
            score = 1
            ANS += score
        else:
            score +=1
            ANS += score
print(ANS)

'''
while L:
    i = L.pop(0)
    if i == 0:
        score = 0
    else :
        if score == 0:
            score = 1
            ANS += score
        else:
            score += 1
            ANS += score
print(ANS)

