import sys
#sys.stdin=open("input.txt", "rt")
'''
N = int(input())
prize = []
for i in range(N):
    a, b, c = map(int, input().split())
    if a==b and b==c:
        prize.append(10000+a*1000)
    elif (a==b and b!=c):
        prize.append(1000+a*100)
    elif (a==c and a!=b):
        prize.append(1000+a*100)
    elif (b==c and c!=a):
        prize.append(1000+b*100)
    else:
        prize.append(max(a,b,c)*100)

print(max(prize))
'''

n = int(input())
res = 0
for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    if a==b and b==c: # if ~elif 중첩은 제일 좋은? 구문이 if절로
        money = 10000+a*1000
    elif a==b or a==c:
        money = 1000+a*100
    elif b==c:
        money = 1000+b*100
    else:
        money = c*100
    if money > res:
        res=money
print(res)

# 느낀점
# 1. 경우의 수로 접근하는게 아닌, 소거법으로 접근을 할 수도 있네
# 2. 이 문제는 그나마 쉬운 문제였던거 같다

# 배운점
# 1. if~elif 중첩에서는 제일 좋은 구문이 if절로(그 뒤는 소거)
# 2. 정렬이 필요한 문제에서는 input을 str로 받아오고 sort 후에 int로 바꾸는 방법
