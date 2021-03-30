import sys
#sys.stdin=open("input.txt", "rt")
#8:49 start
n = int(input())
a = list(input().split())
def digit_sum(x):
    digits = []
    for i in x:
        res = []
        for j in range(len(i)):
            res.append(int(i[j]))
        digits.append(sum(res))
    return digits

digit = digit_sum(a)
cnt = -2149000000
idd = []
for idx, i in enumerate(digit):
    if i > cnt:
        idd = idx
        cnt = i

print(int(a[idd]))

#9:12 end
'''
n = int(input())
a = list(map(int, input().split()))
def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10 # 나머지를 sum에 넣고
        x=x//10 # 몫을 다시 x로 대체
    return sum
    
maxnum = -2147000000
for x in a:
    tot = digit_sum(x)
    if tot>maxnum:
        maxnum=tot
        res=x
print(res)

또는

def digit_sum(x):
    sum=0
    for i in str(x): # int로 된 x를 str로 변환하면 각 자릿수마다 str로 바뀜
        sum += int(i) # 위의 i를 int로 다시 변환해서 sum에 더하면
    return sum # 각 자릿수마다 더한게 된다
'''        

# 느낀점
# 1. 처음에 str로 받아와서 int로 바꾸면서 했는데, 틀린건 아니었나보다
# 2. 그래도 int로 처음에 받아오면 좀 더 편리하다
# 3. 리스트 자체를 변환하는 방법 vs 원소마다 변환하는 방법 뭐가 더 좋을까?

# 배울점
# 1. while로 자릿수 변환방법(나머지 더하고, 몫으로 다시 바꾸고)
# 2. python은 기존 int를 str로 변환하면 for문으로 각 원소마다 접근 가능
 


















