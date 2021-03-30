import sys
#sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())

cnt = 0
for i in range(1, n+1):
    if n%i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else: # break 하지 못한 경우 -> 약수 개수보다 k가 클 경우
    print(-1)
