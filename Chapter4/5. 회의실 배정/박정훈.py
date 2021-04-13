import sys

#sys.stdin=open('input.txt','rt')

n = int(input())
times = list()
for _ in range(n):
    times.append(list(map(int,input().split())))

times = sorted(times)

temp = list()
cnt = 1


for i in range(n-1):
    end_time = times[i][1]
    for j in range(i+1,n):
        if times[j][0] >= end_time:
            end_time = times[j][1]
            cnt += 1
        else :
            end_time = end_time
    temp.append(cnt)

print(max(temp))


'''
정렬
meeting.sort(key = lamnbda x: (x[1], x[0]))

'''
