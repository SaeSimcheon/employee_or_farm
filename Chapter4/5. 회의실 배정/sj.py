import sys
sys.stdin = open("input.txt", "rt")
'''n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort(key = lambda x:x[1]) # 이차원 리스트 정렬방법
meeting = []
current = a[0]
meeting.append(current)
for i in range(1,n):
    if a[i][0] >= current[1]:
        meeting.append(a[i])
        current = a[i]
print(len(meeting))
'''
# 처음에 문제 접근 방법을 모르겠어서 강의 앞부분 보고 시작,,
# 첫시도 100
# 그리디 알고리즘은 무조건 정렬 문제, 정렬 먼저하고 탐색을 하는식으로
# 그 단계에서 가장 좋은것을 선택하는게 그리디 문제

n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e)) # tuple로 저장
meeting.sort(key=lambda x : (x[1],x[0])) # tuple 구조를 바꿔서 정렬하겠다...
et = 0
cnt = 0
for s, e in meeting:
    if s>=et:
        et = e
        cnt += 1

# 느낀점
# 1. 처음에 문제 접근 방식을 어떻게 해야하나 헤맸다 - 종료와 시작시간 사이의 비교
# 2. 튜플로 받아오고 정렬하는건 안가르쳐줬는데 이렇게 하네

# 배운점
# 1. 그리디 문제는 해당 step에서 최적값찾기 / 선정렬 후탐색
# 2. 이차원 리스트 정렬하기 .sort(key = lambda x:x[1])
# 3. tuple로 받아와서 정렬하기