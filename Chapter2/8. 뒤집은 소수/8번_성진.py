import sys
#sys.stdin=open("input.txt", "rt")
# 10:02
n = int(input())
a = list(map(int, input().split()))

def isPrime(x):
    if x<2:
        return False

    else:
        for i in range(2,x):
            if x%i==0:
                return False
        return True

def reverse(x):
    y = 0
    while x>0:
        t = x%10
        y = y*10+t
        x = x//10
    return y

res = []
for i in a:
    j = reverse(i)
    if isPrime(j):
        print(j, end=' ')

# 10:38
'''
def reverse(x):
    res=0
    while x>0:
        t = x%10
        res = res*10 + t
        x = x//10
    return res
def isPrime(x):
    if x==1:
        return False
    else:
        for i in range(2,x//2+1):#소수는 약수가 절반까지만 돌아도 된다/절반 이상이면 나머지가 약수
            if x%i == 0:
                return False
        else: #for가 정상적으로 돌았다면, 마지막에 else로 마지막 반환값 적어주기
            return True
for x in a:
    tmp=reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')
'''
# 느낀점
# 1. 답안 자체는 비슷했다
# 2. 소수는 나누는 수를 절반까지만 계산해도 OK

# 배울점
# 1. 이전에 쓰인 알고리즘이 계속 활용되는거 염두해야겠다
# 2. 자릿수 더하기, 자릿수 바꾸기에서 쓰인 자릿수 다루는 방법 기억해두자
# 3. for else 구문 잘 생각해두기









