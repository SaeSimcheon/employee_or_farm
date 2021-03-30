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

list_below_n=[0]*(n+1)
cnt = 0
for i in range(2,n+1):
    if list_below_n[i] == 0 :
        for j in range(i,n+1,i):
            list_below_n[j] = 1


def isPrime(element,vec):
    if element in vec :
        return element
    else :
        return 0
    
selected=list(map( lambda x :isPrime(x,vec = caster),reversedd))
Primes = [x for x in selected if x != 0]

print(*Primes)
# 40 점 소수 판별하는 부분 개선 요구