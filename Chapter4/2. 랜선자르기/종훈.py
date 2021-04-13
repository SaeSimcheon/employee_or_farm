import sys
#sys.stdin = open("input.txt", "rt")

# 이분탐색 문제는 답이 특정 범위 안에 있다는 것을 알 수 있는 경우에 사용 
k, n = map(int, input().split())
Line = []
res = 0
largest = 0
for i in range(k):
    tmp = int(input())
    Line.append(tmp)
    largest = max(largest, tmp)

lt = 1
rt = largest

def Count(len):
    cnt = 0
    for x in Line:
        cnt += x//len
    return cnt

while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= n:
        res = mid
        lt = mid + 1 # 답이더라도 더 좋은 답을 찾아 나가야 함
    else:
        rt = mid - 1

print(res)

'''
n, m = map(int, input().split())
lines = []
for _ in range(n):
    lines.append(int(input()))

a = sum(lines)//m

while True:
    cnt = 0
    for i in range(len(lines)):
        cnt += lines[i]//a
    if cnt == m:
        break
    elif cnt < m:
        a -= 1
# 시간초과로 40점


print(a)
'''
