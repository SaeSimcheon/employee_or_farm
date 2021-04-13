import sys
sys.stdin = open("input.txt", "rt")
'''k, n = map(int, input().split())
a = [int(input()) for _ in range(k)]
lt = 1
rt = max(a)
highest = 0
while lt<=rt:
    cnt = 0
    mid = (rt+lt)//2
    for i in range(k):
        cnt += a[i]//mid
    if cnt >= n:
        highest = mid
        lt = mid+1
    else:
        rt = mid-1
print(highest)'''

# 이분검색은 결정알고리즘 방법론에서 사용
# 특징 1. 답이 특정 범위안에 존재한다는걸 알 수 있음 -> 범위내에 답이 있는걸 정하고 이분탐색
# 답이 될수있는지 아닌지 확인하는 함수가를 만들어놓아야함
# 답이 안되면 범위를 좁히고, 남은 답중에 좋은 조건을 찾아야
# n보다 작으면 rt를 mid 이상은 안되게 / 크면 lt를 mid 이하는 안되게
def Count(len):
    cnt = 0
    for x in Line:
        cnt += (x//len)
    return cnt

k, n = map(int, input().split())
Line = []
res = 0
largest = 0
for i in range(k):
    tmp=int(input())
    Line.append(tmp)
    largest = max(largest, tmp)
lt = 1
rt = largest
while lt<=rt:
    mid = (lt+rt)//2
    if Count(mid)>=n:
        res = mid
        lt = mid+1
    else:
        rt = mid-1
print(res)

# 느낀점
# 1. 함수를 미리 만들어놓는거도 좋겠다
# 2. 해답 코드는 좀 줄여도 괜찮은거 같다

# 배울점
# 1. 아직 이분검색이 잘 이해는 안감 / 답은 맞았는데, 제대로 알고 짠게 아니라 좀 애매하다
# 2. 이분검색 써야하는 문제 잘 기억해두기 답이 특정 범위안에 존재한다는걸 알고있을때 & 최적의 답을 찾을때
