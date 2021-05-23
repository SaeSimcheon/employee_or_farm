import sys
#sys.stdin = open('input.txt','r')
n = int(input())
dy = [[0]*n for _ in range(n)]
while True:
    a, b = map(int,input().split())
    if a>0 and b>0:
        dy[a-1][b-1] = 1
        dy[b-1][a-1] = 1
    else:
        break
for i in range(n):
    for j in range(n):
        if i!=j and dy[i][j]==0:
            dy[i][j] = 100
for k in range(n):
    for i in range(n):
        for j in range(n):
            dy[i][j] = min(dy[i][j],dy[i][k]+dy[k][j])
candidate = []
for i in dy:
    candidate.append(max(i))
print(min(candidate), candidate.count(min(candidate)))
for i in range(n):
    if candidate[i]==min(candidate):
        print(i+1, end = ' ')

# 첫시도 100
# 문제 이해만 잘하면 푸는건 그렇게 어렵진 않았음
# 근데 문제 이해하는게 조금 힘들다 / 친구가 되는 점수를 계산하는게 중요한듯

# directed graph라면 어떻게 풀까 undiagonal도 모두 고려하는게 필요할거 같다