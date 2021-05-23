import sys
#sys.stdin = open('input.txt','r')
n = int(input())
a = list(map(int,input().split()))
m = int(input())
dy = [0]+[100]*(m)
for i in range(n):
    for j in range(m+1):
        if a[i]<=j:
            dy[j] = min(dy[j],dy[j-a[i]]+1)
print(dy[m])

# 첫시도 100
# 간단하구만
# 이전 문제와 똑같은 풀이 / 근데 처음에 dy를 100으로 초기화를 시킨(최소값 문제)

import sys
sys.stdin = open("input.txt", 'r')
if __name__=="__main__":
    n=int(input())
    coin=list(map(int, input().split()))
    m=int(input())
    dy=[1000]*(m+1);
    dy[0]=0
    for i in range(n):
        for j in range(coin[i], m+1):
            dy[j]=min(dy[j], dy[j-coin[i]]+1)
    print(dy[m])