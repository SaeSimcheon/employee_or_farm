import sys
#sys.stdin=open("input.txt", "rt")

n,m= map(int, input().split())

summ = []

for i in range(1, n+1):
    for j in range(1, m+1):
        summ.append(i+j)
summ.sort()
s = set(summ)
s = list(s)

p = []
for j in s:
    cnt = 0
    for x in summ:
        #cnt = 0
        if x == j:
            cnt += 1
    p.append(cnt)
a = max(p)
for idx, x in enumerate(s):
    if p[idx] == a:
        print(x,end=' ')

#소요시간 : 32분
'''

n,m= map(int, input().split())
cnt = [0] * (n+m+3) # r에서 rep(0,n+m+3) 역할
max = -2147000000 # 가장 작은값으로 초기화
for i in range(1,n+1):
    for j in range(1,m+1):
        cnt[i+j]+=1
for i in range(n+m+1):
    if cnt[i]>max:
        max=cnt[i]
for i in range(n+m+1):
    if cnt[i]==max:
        print(i, end=' ')
'''

#1 : 소요시간이 좀 많이 걸린다, 적응되면 빨리빨리 짜보려고 하자
#2 : 첫번째 for문에서 indexing 으로 바로 count할 수가 있었네 / 다시보니까 코드 개비효율적이야
#3 : r에서 rep(0,n+m)하는거처럼 특정 숫자 반복은 그냥 [0]*(n+m)으로 할 수 있다
#결론 : 코드가 많이 비효율적이다 / 생각을 좀 단순하게 접근해보자 / indexing 잘 생각하면서 해보자
















