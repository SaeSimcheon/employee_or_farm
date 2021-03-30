import sys

#sys.stdin=open("input.txt", "rt")

n = int(input())
a = list(map(int,input().split()))

mean = round(sum(a)/n)
ab = []
for i in a:
    ab.append(abs(i-mean))

ind = []
for j in range(n):
    if ab[j] == min(ab):
        ind.append(j)

so = []
for i in ind:
    so.append(a[i])

for i in range(n):
    if a[i] == max(so):
        print(mean," ",i+1)
        break
'''
답안

n = int(input())
a = list(map(int,input().split()))

ave = round(sum(a)/n)
min = 2147000000 # 큰 수로 임의 설정
for idx, x in enumerate(a): #enumerate : list의 index와 값을 동시에 호출
    tmp = abs(x-ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx+1
    elif tmp == min:
        if x > score:
            score = x
            res = idx+1
print(ave, res)  
'''

# 1 : 최소값 구하기 에서 처럼 처음에 비교대상 수를 정하기
# 2 : enumerate -> 이거 안쓰니까 for문 남발(abs 구하고, abs index 맞는 a값 구하고, 가장 큰 점수 구하고....)
# 3 : 코드를 좀더 효율적으로 짜야겠다 -> 그러러면 함수들 잘 이용해야겠다



'''
대표값 오류 문제 수정
round는 round_half_even 방식
우리가 생각하는건 round_half_up

a= 4.500
print(round(a)) 결과가 4가 나온다.(정확하게 half이면 짝수로 근사값 적용)

따라서
a = 66.5
a = a+0.5 # half일때 첫자리수 올라가고, half 아래면 첫자리수가 안올라간다
a = int(a)
print(a) 










