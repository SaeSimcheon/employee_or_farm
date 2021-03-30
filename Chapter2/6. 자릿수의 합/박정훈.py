import sys

#sys.stdin=open('input.txt','rt')

n = int(input())

numbs = list(map(int, input().split()))
sum_digits = list()

def digit_sum(x):
    for i in range(len(x)):
        numb = numbs[i]
        numb = str(numb) #str로 바꾸고 다시 int
        num = list()
        for j in range(len(numb)):
            num.append(int(numb[j])) #str 값 하나하나 int로 해서 더하기
        sum_digits.append(sum(num))


    max_value = -2147000000
    index = 0
    for i in range(len(sum_digits)):
        if max_value < sum_digits[i]:
            index = i
    return x[index]

print(digit_sum(numbs))

