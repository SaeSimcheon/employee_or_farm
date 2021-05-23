import sys
#sys.stdin = open('input.txt','r')
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
a = sorted(a, key=lambda x: (x[0], x[2]), reverse=True)
dy = [0]*n
#print(a)
dy[0] = a[0][1]
for i in range(1,n):
    H = 0
    for j in range(i-1,-1,-1):
        if a[j][0]>a[i][0] and a[j][2]>a[i][2] and dy[j]>H:
            H=dy[j]
    dy[i] = H+a[i][1]
print(max(dy))

# 첫시도 100
# 이전까지 문제랑 비슷한 유형
# 기준이 두개인 만큼 처음에 내림차순 정렬로 만들어주고
# 첫 벽돌을 답으로 시작하면 OK

import sys
sys.stdin = open("input.txt", 'r')
if __name__=="__main__":
    n=int(input())
    bricks=[]
    for i in range(n):
        a, b, c=map(int, input().split())
        bricks.append((a, b, c))
    bricks.sort(reverse=True)
    dy=[0]*n
    dy[0]=bricks[0][1]
    res=bricks[0][1];
    for i in range(1, n):
        max_h=0;
        for j in range(i-1, -1, -1):
            if bricks[j][2]>bricks[i][2] and dy[j]>max_h:
                max_h=dy[j]
        dy[i]=max_h+bricks[i][1]
        res=max(res, dy[i])
    print(res)

# 반성점
# 1. 정렬을 밑면만 하면 넓이만 고려하면 된다
# 코드에 불필요한 부분이 있었다(문제 이해가 덜 된듯)