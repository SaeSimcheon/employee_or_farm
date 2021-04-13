import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
a = list(map(int,input().split()))
a.sort(reverse = True)
m = int(input())
cnt = 0
while cnt<m:
    a[0] -= 1
    a[n-1] += 1
    a.sort(reverse = True)
    cnt+=1
print(max(a)-min(a)) # 여기 sort 된거라 그냥 a[n-1] - a[0] 해도 ㅇㅋ

# 첫 시도 100
# 내림차순 정렬 이후에 큰거 빼고 작은거 더하고 정렬 반복,,,


