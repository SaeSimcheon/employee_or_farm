'''
교육과정 설계

필수과목 >> 꼭 들어야함

따라서 계획에서 필수과목을 찾음
>> -1이 있다 >> 안들은 거임
>> sort 했을 때 변함 >> 순서대로 안들은 거임
'''
import sys


n = input()
k = int(input())
'''
n = "CBA"
l = ["CBDAGE","FGCDAB"]
'''

n_l = list(n)

for idx in range(k):
    L = input()
    temp = [L.find(x) for x in n_l]

    so_temp = sorted(temp,key = lambda x:x)

    if -1 in temp or temp != so_temp:
        print("#{0} NO".format(1+idx))

    else :print("#{0} YES".format(1+idx))
        
'''


'''
