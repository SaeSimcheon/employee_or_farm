import sys
#sys.stdin = open("input.txt", "rt")

# 그리디(Greedy)는 정렬과 동반해서 문제풀이가 된다

n = int(input())
meeting = []
for _ in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))

meeting.sort(key = lambda x : (x[1], x[0]))

et = 0
cnt = 0
for s, e in meeting:
    if s >= et:
        et = e
        cnt += 1

print(cnt)

'''
n = int(input())
time = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    time.append(tmp)
#print(time)
time.sort(key = lambda x : x[1])
#print(time)

t = time[0]
cnt = 1
for i in range(1, n):
    
    if t[1] <= time[i][0]:
        cnt += 1
        t = time[i]
print(cnt)
# 회의 끝나는 시간을 기준으로 정렬해서 첫번째 회의는 무조건 포함되게 했는데 이게 아닌 경우에는...?
'''
    