import sys
#sys.stdin = open('input.txt','r')
n = int(input())
a = list(map(int, input().split()))
dy = [0]*n
dy[0] = 1
for i in range(1,n):
    cnt = 0
    for j in range(i,0,-1): # 이전과 비교해서 큰지 안큰지 비교
        if a[j]<a[i] and dy[j]>cnt:
            cnt = dy[j] # 크면 cnt를 이전 값으로 업데이트해서
    dy[i] = cnt+1
print(max(dy)) # 출력은 dy의 가장 큰 값(이 경우에는 마지막 값이 답이 아님)

# 도저히 모르겠어서 강의 앞부분 보고 풀었음
# 첫시도 100

# 반성점
# 1. DP를 아직도 이해못했음. 강의보고나서 살짝 이해될 정도
# 사실 풀고나서 정확히 왜 답인지는 모르겠다.