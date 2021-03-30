import sys
#sys.stdin=open("input.txt", "rt")
n = int(input())

# 9:17 start

def isprime(x):
    if x < 2 :
        return False

    else :
        for i in range(2,x):
            if x%i == 0:
                return False
        return True

prime = []
for i in range(1,n+1):
    if isprime(i):
        prime.append(i)

print(prime)

# 9:37 end
'''
# 시간 초과라 다시 코딩(검색한 힌트보면서)
def prime(x):
    prime_list = [True] * x
    
    m = int(x**0.5)
    for i in range(2, m+1):
        if prime_list[i] == True:
            for j in range(i+i, n, i):
                prime_list[j] = False

    return [i for i in range(2,x) if prime_list[i]==True]

print(prime(n))
# wrong answer / 뭐가 잘못된거지?

#소수를 구하는 방법 중 가장 빠른게 에라토스테네스 체
#2의 배수 거르고, 3의 배수 거르고, 5의 배수 거르고...
ch = [0] * (n+1) # index 번호까지 0으로 list 만들기
cnt = 0
for i in range(2,n+1):#2부터 소수인지 아닌지 확인
    if ch[i]==0:
        cnt+=1 # 처음 2는 소수
        for j in range(i, n+1, i): # range의 3번째 input은 배수
            ch[j] = 1
print(cnt)
'''
# 느낀점
# 1. 문제를 잘 읽고 풀자(개수 출력인데 리스트 출력했음)
# 2. 이런 알고리즘을 알아야 문제를 풀 수가 있는게 난감했다
# 3. 알고리즘 속도도 중요하다는 것을 깨달았다

# 배운점
# 1. False 또는 0로 된 벡터에서 찾을 대상만 True or 1로 바꿔주는 방식
# 2. 에라토스테네스 체
# 3. 찾는 대상마다 카운팅하는걸 잘 익히자
# 4. range(i, j, k)에서 k는 배수
