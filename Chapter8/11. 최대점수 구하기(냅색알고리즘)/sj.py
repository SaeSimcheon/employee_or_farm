import sys
#sys.stdin = open('input.txt','r')
n, m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
dy = [0]*(m+1)
'''for i in range(n):
    for j in range(m+1):
        if a[i][1]<=j:
            dy[j] = max(dy[j],dy[j-a[i][1]]+a[i][0])
print(dy[m])'''

# 첫시도 20
# 예제는 맞는데 다른 문제는 틀리게 나온다?
# dy 마지막 값들이 더 크게 나온다 두번째 반복에서 뭔가 있나

for i in range(n):
    for j in range(m, a[i][1]-1, -1):
        dy[j] = max(dy[j],dy[j-a[i][1]]+a[i][0])
print(max(dy))

# 두번째 100
# 반복문 수정하니까 다 맞았음
# 근데 위랑 아래랑 똑같은 구조 아닐까 왜 답이 다르게 나오지
# 뒤에서부터 도는거랑 앞에서부터 도는거랑 차이가 있는걸까
# -> 강의보고 이해함 / 문제를 한문제밖에 못푼다!

import sys
sys.stdin = open("input.txt", 'r')
if __name__=="__main__":
    n, m=map(int, input().split())
    dy=[0]*(m+1);
    for i in range(n):
        ps, pt=map(int, input().split())
        for j in range(m, pt-1, -1):
            dy[j]=max(dy[j], dy[j-pt]+ps)
    print(dy[m])


# 반성점
# 1. 문제 이해를 제대로 못했다

# 배운점
# 1. 문제를 하나밖에 못푸는 것과 같은 문제는 처음에 이차원 테이블로 접근한다
# 업데이트되는 부분부터 dy를 비교해가면서 업데이트를 한다
# 근데 실제로 코드 구현시에는 메모리 저장문제 때문에 일차원 테이블로 접근하면서,
# 문제마다 dy를 업데이트하는 식으로 접근한다.
