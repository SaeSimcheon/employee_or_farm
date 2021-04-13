import sys
#sys.stdin = open("input.txt", "rt")
n, c = map(int, input().split())
'''xi = [int(input()) for _ in range(n)]
xi.sort()
def Count(dist):
    cnt = 1
    horse = xi[0]
    for i in range(1,n):
        if xi[i]-horse>=dist:
            cnt+=1
            horse = xi[i]
    return(cnt)
lt = 1
rt = max(xi)
maximum = 0
while lt<=rt:
    mid = (lt+rt)//2
    if Count(mid)>=c:
        maximum = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(maximum)
'''# 잘 모르겠어서 힌트보고 풀었음...

# 마구간 정렬이 선행
# 3마리가 안되고 그 미만이면 답이 안됨 -> 범위를 줄인다
# 무조건 1에 놓는게 맞는거 같긴한데,,,,
def Count(len):
    cnt=1
    ep=Line[0] # 첫번째 마구간에 처음말을 무조건 배치
    for i in range(1, n):
        if Line[i]-ep>=len:
            cnt+=1
            ep = Line[i]
    return cnt
Line = []
for _ on range(n):
    tmp = int(input())
    Line.append(tmp)
Line.sort()
lt = 1
rt = Line[n-1]
res = 0
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=c:
        res=mid
        lt = mid+1
    else:
        rt = mid-1
print(res)

# 느낀점
# 1. 문제가 잘 이해가 안갔다. 문제 이해가 먼저인거 같다 -> 문제에서 찾고자 하는걸 먼저 찾기
# 2. 처음 마구간에 말을 배치하는게 이해는 가는데 설명내용이 띠용하다

