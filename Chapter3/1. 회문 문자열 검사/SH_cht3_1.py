import sys
sys.stdin = open("cht3_1_input.txt","rt")

n=int(input())

for i in range(n):
    one_man=list(input().lower())
    if one_man == one_man[::-1] :
        print("#{0} YES".format(i+1))
    else : 
        print("#{0} NO".format(i+1))


# 모두 소문자로 전환
# list 간의 비교는 == 만으로 가능하다
# format 사용
# cht2때 배운 ::-1사용해봄