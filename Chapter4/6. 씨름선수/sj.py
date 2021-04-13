import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
'''
a = [list(map(int,input().split())) for _ in range(n)]
a.sort(key = lambda x:x[0],reverse = True)
member = []
player = a[0]
member.append(player)
for i in range(1,n):
    if player[0] > a[i][0] and player[1] > a[i][1]:
        continue
    else:
        member.append(a[i])
        player = a[i]
print(len(member))
'''
# 첫시도는 0점 : 본래 오름차순으로 정렬을 하다보니까 두개를 동시에 비교하기 힘들어지더라
# 두번째 시도는 100점 : 그럼 내림차순으로 정렬 후에 and조건으로 한번에 비교하는 식으로?
# 즉 A(기존)가 B(지원자)가 키도 크고 몸무게도 무거우면 그대로, 그외 경우는 넣어주기
# 아예 큰 조건을 하나 잡으면 하나의 조건만으로 비교가 가능하니까

# 두개 조건 비교가 아니라 하나를 fix해서 하나 조건 비교로만 문제 풀기
body=[]
for i in range(n):
    a, b =map(int, input().split())
    body.append((a,b))
body.sort(reverse = True)
largest = 0
cnt = 0
for x,y in body:
    if y>largest:
        largest=y
        cnt+=1
print(cnt)

# 느낀점
# 1. 문제 디게 간단하게 푸네
# 2. 두개 조건이라고 해도 하나를 고정하면 하나 조건으로만 풀 수 있음

# 배운점
# 1. 직접 list에 넣어서 비교하기 보다는 기준값 갱신 / count +1 해서 코드를 간단하게