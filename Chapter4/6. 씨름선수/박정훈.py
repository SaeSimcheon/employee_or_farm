import sys

#sys.stdin=open('input.txt','rt')
'''
n = int(input())
inform = list()
for _ in range(n):
    inform.append(list(map(int,input().split())))

inform = sorted(inform)

cnt = 1
for i in range(n):
    tmp = inform[i]
    for j in range(1,n):
        if tmp[1] >= inform[j][1]:
            cnt += 1

print(cnt)

'''
#정렬
#meeting.sort(key = lamnbda x: (x[1], x[0]))

n = int(input())
body = []
for i in range(n):
    a, b = map(int,input().split())
    body.append((a,b))

body.sort(reverse=True)
largest = 0
cnt = 0
for x,y in body:
    if y > largest :
        largest = y
        cnt += 1

print(cnt)


#'''
