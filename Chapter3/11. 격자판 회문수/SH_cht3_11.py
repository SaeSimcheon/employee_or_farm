import sys
sys.stdin = open("cht3_11_input.txt","rt")

matrix = list()
for i in range(7):
    matrix.append(list(map(int,input().split())))

def checker(element):
    return element == element[::-1]

def deeper_checker_sum(element):
    return sum(list(map(checker,element)))

def generator(element):
    a = element[0:5]
    b = element[1:6]
    c = element[2:7]
    return [a,b,c]


inv=map(list,zip(*matrix))

org_generated=list(map(generator,matrix))
inv_generated=list(map(generator,inv))

org_sum=list(map(deeper_checker_sum,org_generated))
inv_sum=list(map(deeper_checker_sum,inv_generated))

answer = sum(org_sum) + sum(inv_sum)

print(answer)