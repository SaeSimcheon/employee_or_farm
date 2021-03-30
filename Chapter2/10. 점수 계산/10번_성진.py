import sys
#sys.stdin=open("input.txt", "rt")
#8:24
'''
N = int(input())
a = list(map(int, input().split()))
point = 0

for i in range(N):
    if a[i] == 0:
        point += 0
    elif a[i]==1 and i==0:
        point += 1
    elif a[i]==1 and a[i-1]==0:
        point += 1
    elif a[i]==1 and a[i-1]==1 and a[i-2]==0:
        point += 2
    else:
        for k in range(i):
            if (a[i]==1) and (a[k:i]==[1]*(i-k)):
                point += i-k
            else:
                point += 0
print(point)
'''
# 노느라 9:57 ㅋ

N = int(input())
a = list(map(int, input().split()))
sum = 0
cnt = 0 # 가중치
for x in a:
    if x == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0
print(sum)

# 느낀점
# 1. 괜히 복잡하게 생각해버렸다, 경우의 수로 접근하는게 안좋을 때도 있네
# 2. 가중치 예전에 했던거 같은데 왜 기억이 안났을까...

# 배운점
# 1. 복잡하게 생각하지말자. 경우의수 원툴로 접근하면 비효율적이다
# 첫 접근을 간단하게 하자.
# 2. 가중치(count)로 접근하는거에 익숙해지자(for문 횟수마다 cnt라고 생각하면 될 것 같다)
