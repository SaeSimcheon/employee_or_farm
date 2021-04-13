import sys
#sys.stdin = open("input.txt", "rt")
'''n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
for idx, i in enumerate(a):
    if i == m:
        print(idx+1)'''
# 첫 시도 100
# 이분검색이 뭐야? 그냥 해도 되는건가????
# 강의를 듣고 판단해보자

# lt(맨 왼쪽) & rt(맨 오른쪽) 범위가 필요함
# mid 중간 지점 변수를 다음과 같이 만든다, mid = lt+rt//2
# a[mid] == m인지 찾기 / 아니면? m보다 크면?
# 정렬되어있는 상황이 중요, 그럼 내가 찾고자 하는 값은 mid보다 작은 범위에 있겠군
# 그 이외 범위는 버리고, rt=mid-1 로 새롭게 정의해서 0~2로 범위를 줄이기
# 만약 87이면, lt = mid+1로 그 이외 범위는 버리는 식으로 좁혀나가기
# 계속해서 절반을 버리면서 탐색 범위가 줄어드는 효과 log_2(n)번만에 해결할 수 있대
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
lt = 0
rt = n-1
while lt<=rt:
    mid = (lt+rt)//2
    if a[mid]==m:
        print(mid+1)
        break
    elif a[mid]>m:
        rt = mid-1
    else:
        lt = mid+1

