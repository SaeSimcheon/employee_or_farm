import sys

#sys.stdin=open('input.txt','rt')

n1 = int(input())

list1 = list(map(int, input().split()))

n2 = int(input())

list2 = list(map(int, input().split()))

c = list()

p1 = 0
p2 = 0
            
while p1 < n1 and p2<n2 :
    if list1[p1]<=list2[p2]:
        c.append(list1[p1])
        p1+=1
    else :
        c.append(list2[p2])
        p2+=1
if p1<n1:
    c = c+list1[p1:]
if p2<n2 :
    c = c+list2[p2:]

print(c)
