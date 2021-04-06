import sys
sys.stdin = open("cht3_5_input.txt","rt")

indicator = list(map(int,input().split()))
seq = list(map(int,input().split()))
#print(interval,seq)

sum_seq = list()


#double list comprhension을 통하여 sub sequence의 길이에
#따른 모든 경우의 수에 대해서 합을 구함.
#indicator에 첫째줄 input을 list형태로 할당

sum_seq=[sum(seq[x:(x+i)]) for i in range(1,indicator[0]) for x in range(indicator[0]-i+1)]


# 이후 checker라는 함수를 만들어서 M과 동일한지에 따라 boolean을 반환
# list 와 map을 활용

def checker(element):
    return element == indicator[1]

out=list(map(checker,sum_seq))
print(sum(out))