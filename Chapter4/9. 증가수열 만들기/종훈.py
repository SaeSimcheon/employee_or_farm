import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

lt = 0
rt = n-1

last = 0
res = ""
tmp = []

while lt <= rt:
    if a[lt] > last:
        tmp.append((a[lt], 'L'))
    if a[rt] > last:
        tmp.append((a[rt], 'R'))
    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        res = res + tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    tmp.clear()

print(len(res))
print(res)

'''
n = int(input())
list = list(map(int, input().split()))

a = []
b = []

if list[0] > list[-1]:
    a.append(list[-1])
    list.pop()
    b.append("R")
else:
    a.append(list[0])
    list.pop(0)
    b.append("L")

for i in range(n):
    if len(list) == 1 and a[i] < list[0]:
        a.append(list[0])
        b.append("L")
    elif len(list) == 1 and a[i] > list[0] : 
        break
    
    if list[0] > list[-1] and list[-1] >= a[i]:
        a.append(list[-1])
        list.pop()
        b.append("R")
    elif list[0] < list[-1] and list[0] >= a[i]:
        a.append(list[0])
        list.pop(0)
        b.append("L")
    else:
        break

print(len(a))
for i in range(len(b)):
    print(b[i], end = '')
'''