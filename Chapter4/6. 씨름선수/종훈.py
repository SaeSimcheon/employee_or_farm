import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
body = []

for _ in range(n):
    a, b = map(int, input().split())
    body.append((a, b))

body.sort(reverse = True)

largest = 0
cnt = 0

for x, y in body:
    if y > largest:
        largest = y
        cnt += 1
print(cnt)


'''
n = int(input())
people = []
for _ in range(n):
    k, m = map(int, input().split())
    people.append((k, m))

people.sort()

cnt = 0
for i in range(n):
    for j in range(i+1, n):
        if people[i][1] < people[j][1]:
            break
    else:
        cnt+=1

print(cnt)

# 이거 내꺼 쫌 괜찮은 듯?
# 키 작은 순서대로 정렬해놓고 몸무게만 비교
# 작은 순서니까 아래순서에 있는 사람보다 몸무게가 작으면 탈락
# 아랫사람들과 두번째 for문으로 하나씩 비교하면서 몸무게가 큰 사람이 나오면 break
# break 되지 않고 끝까지 두번째 for문이 완료되면 else를 통해 cnt +1
'''