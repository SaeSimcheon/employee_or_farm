import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

p1 = p2 = 0
c = []

while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1

if p1 < n:
    c = c + a[p1:]
if p2 < m:
    c = c + b[p2:]

for x in c:
    print(x, end = ' ')


'''
n1 = int(input())
list1 = list(map(int, input().split()))

n2 = int(input())
list2 = list(map(int, input().split()))

p1 = 0
p2 = 0
list = []


while p1 == (n1-1) or p2 == (n2-1):
    if list1[p1] <= list2[p2]:
        list.append(list1[p1])
        p1 += 1
    else:
        list.append(list2[p2])
        p2 += 1
list.append(list1[p1:])
list.append(list2[p2:])
 
for i in list:
    print(i, end = ' ')

'''

'''
n1 = int(input())
list1 = list(map(int, input().split()))

n2 = int(input())
list2 = list(map(int, input().split()))

for i in sorted(list1+list2):
    print(i, end=' ')
'''