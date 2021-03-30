import sys
sys.stdin = open("cht2_8_input.txt","rt")

n=int(input())

seq=list(map(int,input().split()))


def reverse(element):
    element_seq=list(str(element))
    element_seq.reverse()
    select = element_seq.index(next(filter(lambda x: x!="0", element_seq)))
    select_element=element_seq[select:]
    return int("".join(select_element))


reversedd=list(map(reverse,seq))

list_below_n=list(range(1,max(reversedd)+1))
caster = list()
#print(list_below_n)
while len(list_below_n) != 0 :
    divider=list_below_n.pop(0)
    if divider == 1 :
        pass
    else:
        list_below_n = [x for x in list_below_n if x % divider !=0]
        caster.extend([divider])


def isPrime(element,vec):
    if element in vec :
        return element
    else :
        return 0
    
selected=list(map( lambda x :isPrime(x,vec = caster),reversedd))
Primes = [x for x in selected if x != 0]

print(*Primes)
# 40 점 소수 판별하는 부분 개선 요구